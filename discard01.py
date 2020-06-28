# from threading import Timer
# switch = True
#
# def lemon():

arr = []

for i in range(10000):
    arr.append(i)

print(arr)



#     while switch:
#         for i in range(1000000000):
#             for j in range(1000000000):
#                 for k in range(1000000000):
#                     for l in range(1000000000):
#                         for m in range(1000000000):
#                             for n in range(1000000000):
#                                 num = i + j + k + l + m + n
#                                 if not num % 5023173:
#                                     print(num, switch)
#
#
#
#
# def off():
#     global switch
#     switch = False
#
#
# t = Timer(5.0, off)
# t.start()
#
#
# lemon()