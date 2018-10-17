from helpers import generate_classes_from_string
from instructions.base_instructions import Cmp, And, Or, Eor, Adc, Cpy, Cpx, Sbc

types = []


# CMP

cmp_types = '''
immidiate     CMP #oper     C9    2     2
zeropage      CMP oper      C5    2     3
zeropage,X    CMP oper,X    D5    2     4
absolute      CMP oper      CD    3     4
absolute,X    CMP oper,X    DD    3     4*
absolute,Y    CMP oper,Y    D9    3     4*
(indirect,X)  CMP (oper,X)  C1    2     6
(indirect),Y  CMP (oper),Y  D1    2     5*
'''

for generated in generate_classes_from_string(Cmp, cmp_types):
    types.append(generated)


# CPY

cpy_types = '''
immidiate     CPY #oper     C0    2     2
zeropage      CPY oper      C4    2     3
absolute      CPY oper      CC    3     4
'''

for generated in generate_classes_from_string(Cpy, cpy_types):
    types.append(generated)


# CPX

cpx_types = '''
immidiate     CPX #oper     E0    2     2
zeropage      CPX oper      E4    2     3
absolute      CPX oper      EC    3     4
'''

for generated in generate_classes_from_string(Cpx, cpx_types):
    types.append(generated)

# AND

and_types = '''
immidiate     AND #oper     29    2     2
zeropage      AND oper      25    2     3
zeropage,X    AND oper,X    35    2     4
absolute      AND oper      2D    3     4
absolute,X    AND oper,X    3D    3     4*
absolute,Y    AND oper,Y    39    3     4*
(indirect,X)  AND (oper,X)  21    2     6
(indirect),Y  AND (oper),Y  31    2     5*
'''

for generated in generate_classes_from_string(And, and_types):
    types.append(generated)


# OR

or_types = '''
immidiate     ORA #oper     09    2     2
zeropage      ORA oper      05    2     3
zeropage,X    ORA oper,X    15    2     4
absolute      ORA oper      0D    3     4
absolute,X    ORA oper,X    1D    3     4*
absolute,Y    ORA oper,Y    19    3     4*
(indirect,X)  ORA (oper,X)  01    2     6
(indirect),Y  ORA (oper),Y  11    2     5*
'''

for generated in generate_classes_from_string(Or, or_types):
    types.append(generated)


# XOR

eor_types = '''
immidiate     EOR #oper     49    2     2
zeropage      EOR oper      45    2     3
zeropage,X    EOR oper,X    55    2     4
absolute      EOR oper      4D    3     4
absolute,X    EOR oper,X    5D    3     4*
absolute,Y    EOR oper,Y    59    3     4*
(indirect,X)  EOR (oper,X)  41    2     6
(indirect),Y  EOR (oper),Y  51    2     5*
'''

for generated in generate_classes_from_string(Eor, eor_types):
    types.append(generated)


# ADC

adc_types = '''
immidiate     ADC #oper     69    2     2
zeropage      ADC oper      65    2     3
zeropage,X    ADC oper,X    75    2     4
absolute      ADC oper      6D    3     4
absolute,X    ADC oper,X    7D    3     4*
absolute,Y    ADC oper,Y    79    3     4*
(indirect,X)  ADC (oper,X)  61    2     6
(indirect),Y  ADC (oper),Y  71    2     5*
'''

for generated in generate_classes_from_string(Adc, adc_types):
    types.append(generated)


# SBC

sbc_types = '''
immidiate     SBC #oper     E9    2     2
zeropage      SBC oper      E5    2     3
zeropage,X    SBC oper,X    F5    2     4
absolute      SBC oper      ED    3     4
absolute,X    SBC oper,X    FD    3     4*
absolute,Y    SBC oper,Y    F9    3     4*
(indirect,X)  SBC (oper,X)  E1    2     6
(indirect),Y  SBC (oper),Y  F1    2     5*
'''

for generated in generate_classes_from_string(Sbc, sbc_types):
    types.append(generated)
