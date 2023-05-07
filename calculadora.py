import gmpy2


def suma_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a + b, n)


def multiplicacion_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a * b, n)


def division_modulo(a, b, n):
    a = a % n
    b = b % n
    if gmpy2.gcd(b, n) != 1:
        raise ValueError("No existe el inverso multiplicativo modular")
    return gmpy2.f_mod(a * gmpy2.invert(b, n), n)


def potencia_modulo(a, b, n):
    a = a % n
    return gmpy2.powmod(a, b, n)


def inverso_modulo(a, n):
    a = a % n
    g, x, y = gmpy2.gcdext(a, n)
    if g != 1:
        raise ValueError("No existe el inverso multiplicativo modular")
    return gmpy2.f_mod(x, n)


## Algoritmo de Tonelli-Shanks
def raiz_cuadrada_modulo(a, n):
    if gmpy2.legendre(a, n) != 1:
        return "No existe la raíz cuadrada modular"
    else:
        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        m = 2
        while gmpy2.legendre(m, n) != -1:
            m += 1

        b = gmpy2.powmod(a, (d + 1) // 2, n)
        g = gmpy2.powmod(m, d, n)
        r = gmpy2.powmod(a, d, n)

        for i in range(1, s):
            t = r
            for j in range(1, s - i):
                t = gmpy2.powmod(t, 2, n)
            if gmpy2.powmod(g, 2 ** (s - i - 1), n) == 1:
                b = (b * t) % n
                r = (r * gmpy2.powmod(t, 2, n)) % n
            g = gmpy2.powmod(g, 2, n)

        return (b, n - b)


def lista_cuadrados_modulo(n):
    cuadrados = []
    for i in range(n):
        if gmpy2.legendre(i, n) == 1:
            cuadrados.append(i)
    return cuadrados


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
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
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
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
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
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                resultado = division_modulo(a, b, n)
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
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                resultado = potencia_modulo(a, b, n)
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
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                resultado_a = inverso_modulo(a, n)
                resultado_b = inverso_modulo(b, n)
                print("InvM en a=", resultado_a)
                print("InvM en b=", resultado_b)
            elif eleccion == 6:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                print("Ingresa un número de Zn (a)")
                a = gmpy2.mpz(input())
                a = a % n
                print("Ingresa un número de Zn (b)")
                b = gmpy2.mpz(input())
                b = b % n
                resultado_a = raiz_cuadrada_modulo(a, n)
                resultado_b = raiz_cuadrada_modulo(b, n)
                print("Las raíces cuadradas modulares en n de a son:", resultado_a)
                print("Las raíces cuadradas modulares en n de b son:", resultado_b)
            elif eleccion == 7:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                resultado = lista_cuadrados_modulo(n)
                if len(resultado) > 0:
                    print("CuadradosPerfectosM=", resultado)
                    print("La cantidad de cuadrados perfectos=", len(resultado))
                else:
                    print("No existen cuadrados perfectos en Zn")
            else:
                print("Elección inválida, Intenta otra vez")
        except ValueError as e:
            print("Error:", e)



