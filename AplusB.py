# A, B=input().split()
# sum=int(A)+int(B)
# print(sum)
# def runningsum(input_list:list[int]):
#     output_list=[input_list[0]]
#     for i in input_list[1:]:
#         output_list.append(i+output_list)
#     return output_list
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x=zip(a,b)
for i in x:
    print(i)
