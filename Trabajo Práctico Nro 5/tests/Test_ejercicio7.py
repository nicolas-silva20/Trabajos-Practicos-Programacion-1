import pytest
import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase")
import funciones

@pytest.mark.parametrize('list, res',[
    ([], (None, None)),
    ([1.0, 2.0, 3.0], (3.0, 1.0)),
    ([4.0, 5.0, 8.0], (8.0, 4.0))
])

def test_find_max_min(list, res):
    assert funciones.find_max_min(list) == res