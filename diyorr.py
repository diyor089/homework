   # /1/

def tugilgan_yilini_hisobla():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))

    joriy_yil = 2024
    tugilgan_yil = joriy_yil - yosh

    print(f"{ism}, siz {tugilgan_yil}-yilda tug'ilgansiz.")


tugilgan_yilini_hisobla()


   # /2/

def kvadrat_va_kub():
    son = float(input("Son kiriting: "))
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son} ning kvadrati: {kvadrat}")
    print(f"{son} ning kubi: {kub}")

kvadrat_va_kub()


  # /3/

def qoldiqsiz_bolinish():
    son = int(input("Son kiriting: "))
    for i in (2, 50):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")
        else:
            print(f"{son} {i} ga qoldiqsiz bo'linmaydi.")

qoldiqsiz_bolinish()
