import pytest
from geometria import classificar_triangulo

@pytest.mark.happy_path
@pytest.mark.parametrize("a,b,c", [
    (2, 2, 2),
    (8, 8, 8),
    (5, 5, 5),
])
def test_equilatero(a, b, c):
    assert classificar_triangulo(a, b, c) == "Equilatero"

@pytest.mark.happy_path
@pytest.mark.parametrize("a,b,c", [
    (2, 2, 1),
    (5, 7, 5),
    (6, 10, 10),
    (2, 4, 4),
])
def test_isosceles(a, b, c):
    assert classificar_triangulo(a, b, c) == "Isosceles"

@pytest.mark.happy_path
@pytest.mark.parametrize("a,b,c", [
    (4, 5, 6),
    (10, 11, 12),
    (2, 3, 4),
    (7.5, 8.5, 9.5),
])
def test_escaleno(a, b, c):
    assert classificar_triangulo(a, b, c) == "Escaleno"

@pytest.mark.error_handling
@pytest.mark.parametrize("a,b,c", [
    (1, 2, 4),
    (3, 2, 7),
    (1, 2, 3),      
    (1, 10, 12),    
    (5, 1, 1),      
    (1, 2, 4),      
])
def test_triangulo_invalido(a, b, c):
    with pytest.raises(ValueError, match="Lados não formam um triangulo"):
        classificar_triangulo(a, b, c)

@pytest.mark.error_handling
@pytest.mark.parametrize("a,b,c", [
    ([], 1, -1),
    (None, 2, 2),
    ("a", 3, 3),
    (4, "b", 4),
    (5, 5, "c"),
    ({}, 1, 1),
])
def test_tipo_invalido(a, b, c):
    with pytest.raises(TypeError, match="Os lados devem ser int ou float"):
        classificar_triangulo(a, b, c)

@pytest.mark.error_handling
@pytest.mark.parametrize("a,b,c", [
    (2, -2, 4),
    (-6, 1, 9),
    (3, -4, 2),
    (4, -1, -4),
])
def test_valores_invalidos(a, b, c):
    with pytest.raises(ValueError, match="Os lados devem ser positivos."):
        classificar_triangulo(a, b, c)
