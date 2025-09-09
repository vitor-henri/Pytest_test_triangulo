def classificar_triangulo(a:float, b:float, c:float) -> str:

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError("Os lados devem ser int ou float")

    # Verifica se lados tem valores positivos
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Os lados devem ser positivos.")
    
    # Verifica se a soma de quaisquer os lados devem ser maior que o terceiro lado
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Lados não formam um triangulo")
    if a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Escaleno"