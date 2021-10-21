def suma(x, y):
    """
    Suma los valores pasados como argunmentos y devuelve el resultado se sumarlos
    args:
        x -> Valor númerico (int/float)
        y -> Valor númerico (int/float)
    return x + y
    """
    return x + y


def escribir(fpath, data_in):
    """
    Función que escribe en un archivo
    args:
        fpath -> path absoluto del archivo
        data_in -> información a escribir
    """
    with open(fpath, "w") as file_in:
        file_in.write(data_in)


class Calculadora:
    """
    Clase calculadora
    """

    def sumar(x, y):
        """
        Suma los valores pasados como argunmentos y devuelve el resultado se sumarlos
        args:
            x -> Valor númerico (int/float)
            y -> Valor númerico (int/float)
            return x + y
        """
        return suma(x, y)
