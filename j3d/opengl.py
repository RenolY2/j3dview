import gl
import gx


MATRIX_INDEX_ATTRIBUTE_LOCATION = 0
POSITION_ATTRIBUTE_LOCATION = 1
NORMAL_ATTRIBUTE_LOCATION = 2
BINORMAL_ATTRIBUTE_LOCATION = 3
TANGENT_ATTRIBUTE_LOCATION = 4
COLOR_ATTRIBUTE_LOCATION = 5
TEXCOORD_ATTRIBUTE_LOCATIONS = [6,7,8,9,10,11,12,13]

ATTRIBUTE_LOCATION_TABLE = {
        gx.VA_PTNMTXIDX:MATRIX_INDEX_ATTRIBUTE_LOCATION,
        gx.VA_POS:POSITION_ATTRIBUTE_LOCATION,
        gx.VA_NRM:NORMAL_ATTRIBUTE_LOCATION,
        gx.VA_CLR0:COLOR_ATTRIBUTE_LOCATION,
        gx.VA_CLR1:COLOR_ATTRIBUTE_LOCATION,
        gx.VA_TEX0:TEXCOORD_ATTRIBUTE_LOCATIONS[0],
        gx.VA_TEX1:TEXCOORD_ATTRIBUTE_LOCATIONS[2],
        gx.VA_TEX2:TEXCOORD_ATTRIBUTE_LOCATIONS[2],
        gx.VA_TEX3:TEXCOORD_ATTRIBUTE_LOCATIONS[3],
        gx.VA_TEX4:TEXCOORD_ATTRIBUTE_LOCATIONS[4],
        gx.VA_TEX5:TEXCOORD_ATTRIBUTE_LOCATIONS[5],
        gx.VA_TEX6:TEXCOORD_ATTRIBUTE_LOCATIONS[6],
        gx.VA_TEX7:TEXCOORD_ATTRIBUTE_LOCATIONS[7]}

MATRIX_BLOCK_BINDING_POINT = 0
MATERIAL_BLOCK_BINDING_POINT = 1
MATRIX_TABLE_TEXTURE_UNIT = 0
TEXTURE_UNITS = [1,2,3,4,5,6,7,8]


class MatrixBlock(gl.UniformBlock):
    projection_matrix = gl.mat4
    view_matrix = gl.mat4x3

