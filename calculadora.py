import gmpy2


def suma_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a + b, n)


def multiplicacion_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a * b, n)


def division_modular(dividendo, divisor, modulo):
        try:
            a = gmpy2.mpz(dividendo)
            b = gmpy2.mpz(divisor)
            c = gmpy2.mpz(modulo)

            resultado = gmpy2.f_mod(a // b, c)

            return resultado

        except (ValueError, gmpy2.DivisionByZero):
            print("Error: valores no válidos para la división")
            return None


def potencia_modular(a, b, n):
    a = a % n
    return gmpy2.powmod(a, b, n)


def inversos_multiplicativos_modulo(a, n):
    inversos = []
    for i in range(n):
        if gmpy2.gcd(i, n) == 1:
            if gmpy2.gcd(a, n) == 1:
                inverso = gmpy2.invert(i, n)
                inversos.append(inverso)
    return inversos


def raices_cuadradas_modulares(a, n):
    try:
        a = gmpy2.mpz(a)
        n = gmpy2.mpz(n)

        if gmpy2.legendre(a, n) != 1:
            print("Error: a no es un residuo cuadrático módulo n")
            return None

        raices = []

        raiz = gmpy2.powmod(a, (n + 1) // 4, n)

        if gmpy2.f_mod(gmpy2.square(raiz), n) == a:
            raices.append(raiz)

            if n != 1:
                raices.append(n - raiz)

        return raices

    except ValueError:
        print("Error: valores no válidos para calcular las raíces cuadradas modulares")
        return None

def cuadrados_perfectos_modulo(a, n):
    cuadrados_perfectos = []
    for i in range(n):
        cuadrado = gmpy2.powmod(i, 2, n)
        if cuadrado == a % n:
            cuadrados_perfectos.append(i)
    return cuadrados_perfectos


def main():
    print("Bienvenido a ZCalc\nTu calculadora modular de confianza!")
    while True:
        try:
            print("1. SumaM")
            print("2. MultiplicaciónM")
            print("3. DivisiónM")
            print("4. PotenciaM")
            print("5. Inverso multiplicativoM")
            print("6. Raíz cuadradaM")
            print("7. Lista de cuadrados perfectosM")
            print("0. Salir")
            eleccion = int(input("Ingrese su elección: "))
            if eleccion == 0:
                break
            elif eleccion == 1:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                if b >= 0:
                    b = b
                else:
                    b = abs(b)
                resultado = suma_modulo(a, b, n)
                print("SumaM=", resultado)
            elif eleccion == 2:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                if b >= 0:
                    b = b
                else:
                    b = abs(b)
                resultado = multiplicacion_modulo(a, b, n)
                print("ProductoM=", resultado)
            elif eleccion == 3:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                if b >= 0:
                    b = b
                else:
                    b = abs(b)
                resultado = division_modular(a, b, n)
                print("DivisonM=", resultado)
            elif eleccion == 4:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                if b >= 0:
                    b = b
                else:
                    b = abs(b)
                resultado = potencia_modular(a, b, n)
                print("PotenciaM=", resultado)
            elif eleccion == 5:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                resultado_a = inversos_multiplicativos_modulo(a,n)
                print("InvM=", resultado_a)
                print(len(resultado_a))



            elif eleccion == 6:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                if a >= 0:
                    a = a
                else:
                    a = abs(a)
                resultado_a = raices_cuadradas_modulares(a,n)
                print("Las raíces cuadradas modulares en n de a son:", resultado_a)
            elif eleccion == 7:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n

                resultado = cuadrados_perfectos_modulo(a,n)
                if len(resultado) > 0:
                    print("CuadradosPerfectosM=", resultado)
                    print("La cantidad de cuadrados perfectos=", len(resultado))
                else:
                    print("No existen cuadrados perfectos en Zn")
            else:
                print("Elección inválida, Intenta otra vez")
        except ValueError as e:
            print("Error:", e)