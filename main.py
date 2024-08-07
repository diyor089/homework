buyurtmalar = []
while True:
    buyurtmalar = input("Buyurtma qilish uchun mahsulot nomini kiriting (dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): ")
    if buyurtmalar.lower() in ['exit', 'quit']:
        break
    buyurtmalar.lower()
print("Sizning buyurtmalaringiz: ")