def salom_ber(ism):
    '''Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya'''
    print(f"Assalomu Aleykum!,hurmatli {ism.title()}")


salom_ber('diyorbek')
salom_ber('ali')
salom_ber('vali')




def toliq_ism(ism, familiya):
    """Foydalanuvchini ism va familiyasini jamlab chiqaruvchi dastur"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydaluvchi familiyasi: {familiya.title()}")
toliq_ism("diyorbek", "nurmetov")

def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
    """Foydaluvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(2010)

def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
print(toliq_ism_yasa("diyorbek", "nurmetov"))

talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('diyor','nurmetov')
print(talaba1)
print(talaba2)

def auto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    auto = {'kompaniya':kompaniya,
            'model':model,
            'rang': rangi,
            'karovka': karobka,
            'yil': yili,
            'narh': narhi}
    return auto

avto1 = auto_info('GM','Malibu','qora','avtomat','2023')
print(avto1)

def oraliq(min,max):
    sonlar = []
    sonlar.append(min)
    min += 1
