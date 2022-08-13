def short():
    mya = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    myb = [liczba for liczba in mya if liczba % 2 == 0]
    print(myb)
short()

# def long():
#     mya = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#     myb = []
#     for liczba in mya:
#         if liczba % 2 == 0:
#             myb.append(liczba)
#     print(myb)
# long()

