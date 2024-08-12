

                                    # 1-topshiriq
def summa(*sonlar):
    """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
    kopaytma = 2
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(summa(5,5))
print(summa(6,6))




                                  # 2-topshiriq


def talaba_info(ism, familiya, **kwargs):
  info = {'Ism':ism , 'Familiya': familiya}
  info.update(kwargs)
  return info

print(talaba_info('Ali', 'Valiyev', Yosh=20, Universitet='URDU', Yonalish='Sport'))