import gmpy2
import math


def suma_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a + b, n)


def multiplicacion_modulo(a, b, n):
    a = a % n
    b = b % n
    return gmpy2.f_mod(a * b, n)


def division_modular(a,b,n):
    a = a % n
    b = b % n
    try:
        inv = pow(b,-1, n)
        print(inv)
        if inv != 0:
            return ((a * inv) % n)
    except (ValueError, ZeroDivisionError):
        return "no se puede operar"


def potencia_modular(a, b, n):
    a = a % n
    return gmpy2.powmod(a, b, n)


def inversos_multiplicativos_modulo(n):
    inversos = []
    for i in range(n):
        if gmpy2.gcd(i, n) == 1:
            inverso = gmpy2.invert(i, n)
            inversos.append(inverso)
    return inversos


def raices_cuadradas_modulares(n):
    raices = []
    for i in range(n // 2, 2, -1):
        resto = n % i
        if resto == 0:
            aux = n // i
            if aux == 2 or (aux % 2 != 0 and aux != n and aux != 1):
                raices.append(aux)
    return raices


def cuadrados_perfectos_modulo(n):
        cuadrados_perfectos = []
        for i in range(int(math.sqrt(n)) + 1):
            cuadrado = i * i
            if cuadrado <= n:
                cuadrados_perfectos.append(cuadrado)
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
                print(f"DivisonM= {division_modular(a, b, n)}")

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
                resultado_a = inversos_multiplicativos_modulo(n)
                print("InvM=", resultado_a)
                print(f"la cantidad es: {len(resultado_a)}")



            elif eleccion == 6:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                resultado = raices_cuadradas_modulares(n)
                print("Las raíces cuadradas modulares en n son:", resultado)
            elif eleccion == 7:
                print("Ingresa un número entero positivo (n)")
                n = gmpy2.mpz(input())
                while n <= 0:
                    print("Ingresa un número entero positivo (n)")
                    n = gmpy2.mpz(input())
                resultado = cuadrados_perfectos_modulo(n)
                if len(resultado) > 0:
                    print("CuadradosPerfectosM=", resultado)
                    print("La cantidad de cuadrados perfectos=", len(resultado))
                else:
                    print("No existen cuadrados perfectos en Zn")
            else:
                print("Elección inválida, Intenta otra vez")
        except ValueError as e:
            print("Error:", e)