# # 01
# def compute_tax(money_list):
#     tax = 0
#     for money in money_list:
#         if money >= 200:
#             tax += 20
#         elif money < 200 and money >= 100:
#             tax += 10
#     return tax

# # 02
# t = int(input())
# for i in range(t):
#     price = int(input())
#     money = input().strip().split()
#     money = list(map(int,money))
#     money = [money[0]*1,money[1]*2,money[2]*5,money[3]*10,money[4]*20,money[5]*50 ]
#     print(money)
#     money = sum(money)
#     print(money)
#     if money >= price:
#         print('ANO')
#     else:
#         print('NE')

# # 03
# def check_sudoku(pole):
#     helper = []
#     for znak in pole:
#         if znak in helper or znak not in [1,2,3,4,5,6,7,8,9]:
#             return False
#             break
#         else:
#             helper.append(znak)
#     return True

# # 04
# nm = input().strip().split()
# nm = list(map(int,nm))
# matica = []
# for i in range(nm[0]-1):
#     for j in range(nm[1]-1):
#         matica.append(input().strip().split())
# print(matica)

# # 05
# t = int(input())
# for i in range(t):
#         n = int(input())
#         pole = input().strip().split()
#         pole = list(map(int,pole))
#         out = 0
#         for j in pole:
#             if j%2 == 0:
#                 out += 2
#             else:
#                 out += 3
#         if out/n < 2.5:
#              print('ANO')
#         else:
#              print('NE')

# # 06
# def censor_number(k,n):
#     for i in range(n):
#         if str(k) in str(i):
#             a = str(i)
#             if a[0] == str(k):
#                 print(a[1]'*')
#             else:
#                 print(a[0]'*')
#         else:
#             print(i)
# censor_number(2,35)

# # 06 - correct
# def censor_number(k,n):
#     for i in range(n):
#         if str(k) in str(i):
#             a = str(i)
#             print(a.replace(str(k),'*'))
#         else:
#             print(i)
# censor_number(2,35)

# # 04 - correct
# nm = input().strip().split()
# nm = list(map(int,nm))
# matica = []
# for i in range(nm[0]):
#     matica.append(input().strip().split())
# out = []
# for i in range(nm[1]):
#     pole = []
#     for j in range(nm[0]):
#         pole.append(matica[j][i])
#     out.append(pole)
# print(out)