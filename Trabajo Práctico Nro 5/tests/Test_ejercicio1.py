import pytest
import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase")
import funciones


@pytest.mark.parametrize('a, res',[
    ('43543367', True),
    ('42543876', True),
    ('12345678', True),
    ('541', None),
    ('12345', None),
    ('hola', False)
])

def test_validate_dni(a, res):
    assert funciones.validate_dni(a) == res