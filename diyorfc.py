print("Yaxshi korgan kitoblarni chiqarib beruvchi dastur." )
savol = "Yaxshi korgan kitoblaringizni nomini kirting "
savol += "(dasturni toxtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    kitoblar = input(savol)
    if kitoblar == "exit":
        ishora = False
    else:
        print(kitoblar)


