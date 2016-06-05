import numpy
from OpenGL.GL import *
from PyQt5 import QtCore,QtWidgets
import gl


VERTEX_TYPE = numpy.dtype([('position',numpy.float32,2),('texcoord',numpy.float32,2)])

POSITION_ATTRIBUTE_LOCATION = 0
TEXCOORD_ATTRIBUTE_LOCATION = 1

DISPLAY_TEXTURE_UNIT = 0

VERTEX_SHADER_STRING = """
#version 330

layout(location={POSITION_ATTRIBUTE_LOCATION}) in vec4 position;
layout(location={TEXCOORD_ATTRIBUTE_LOCATION}) in vec2 texcoord;

out vec2 vertex_texcoord;

void main()
{{
    gl_Position = position;
    vertex_texcoord = texcoord;
}}
""".format(**locals())

FRAGMENT_SHADER_STRING = """
#version 330

uniform sampler2D display_texture;
in vec2 vertex_texcoord;
out vec4 fragment_color;

void main()
{
    fragment_color = texture(display_texture,vertex_texcoord);
}
"""


class PreviewWidget(QtWidgets.QOpenGLWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.texture = None

    @property
    def position_array(self):
        return self.vertex_buffer['position']

    @property
    def texcoord_array(self):
        return self.vertex_buffer['texcoord']

    def initializeGL(self):
        vertex_shader = gl.Shader(GL_VERTEX_SHADER,VERTEX_SHADER_STRING)
        fragment_shader = gl.Shader(GL_FRAGMENT_SHADER,FRAGMENT_SHADER_STRING)
        self.program = gl.Program(vertex_shader,fragment_shader)

        glUseProgram(self.program)
        display_texture_location = glGetUniformLocation(self.program,'display_texture')
        glUniform1i(display_texture_location,DISPLAY_TEXTURE_UNIT)

        self.vertex_array = gl.VertexArray()
        glBindVertexArray(self.vertex_array)
        self.vertex_buffer = gl.ManagedBuffer(GL_ARRAY_BUFFER,GL_DYNAMIC_DRAW,4,VERTEX_TYPE)

        offset = VERTEX_TYPE.fields['position'][1]
        glEnableVertexAttribArray(POSITION_ATTRIBUTE_LOCATION)
        glVertexAttribPointer(POSITION_ATTRIBUTE_LOCATION,2,GL_FLOAT,False,VERTEX_TYPE.itemsize,GLvoidp(offset))

        offset = VERTEX_TYPE.fields['texcoord'][1]
        glEnableVertexAttribArray(TEXCOORD_ATTRIBUTE_LOCATION)
        glVertexAttribPointer(TEXCOORD_ATTRIBUTE_LOCATION,2,GL_FLOAT,False,VERTEX_TYPE.itemsize,GLvoidp(offset))

        self.texcoord_array[0,0] = 0
        self.texcoord_array[0,1] = 1
        self.texcoord_array[1,0] = 0
        self.texcoord_array[1,1] = 0
        self.texcoord_array[2,0] = 1
        self.texcoord_array[2,1] = 0
        self.texcoord_array[3,0] = 1
        self.texcoord_array[3,1] = 1

    def set_display_rectangle(self,x0,y0,x1,y1):
        self.position_array[0,0] = x0
        self.position_array[0,1] = y0
        self.position_array[1,0] = x0
        self.position_array[1,1] = y1
        self.position_array[2,0] = x1
        self.position_array[2,1] = y1
        self.position_array[3,0] = x1
        self.position_array[3,1] = y0

    def update_display_rectangle(self):
        if self.texture is None: return
        if self.height() == 0 or self.width() == 0: return

        sw = self.width()/self.height()*self.texture.height/self.texture.width
        sh = self.height()/self.width()*self.texture.width/self.texture.height

        if sw < sh:
            self.set_display_rectangle(-1,-sw,1,sw)
        else:
            self.set_display_rectangle(-sh,-1,sh,1)

    def paintGL(self):
        glClearColor(0,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT)
        if self.texture is not None and self.height() != 0 and self.width() != 0:
            glUseProgram(self.program)
            self.texture.gl_bind(DISPLAY_TEXTURE_UNIT)
            glBindVertexArray(self.vertex_array)
            self.vertex_buffer.sync_data()
            glDrawArrays(GL_TRIANGLE_FAN,0,4)

    def resizeGL(self,width,height):
        glViewport(0,0,width,height)
        self.update_display_rectangle()

    @QtCore.pyqtSlot(object)
    def setTexture(self,texture):
        self.texture = texture
        self.update_display_rectangle()
        self.update()
