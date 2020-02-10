# def is_leap(year):
#     # leap = False
#
#     # Write your logic here
#     if year%4==0 and year%100!=0 or year%400==0:
#         leap=True
#
#         return leap
#     else:
#         return False
#
#
# year = int(input())
# print(is_leap(year))



############################

#
# if __name__ == '__main__':
#     n = int(input())
#
# for i in range(1,n+1):
#     print(i, end='')
#



######################

# list=[]
# string, substring=(input().strip(),input().strip())
# for i in range(3):
#     if string[i:i+len(substring)]==substring:
#         list=list.append(i)
#         print(i)


########################################




# def count_substring(string, sub_string):
#     count=0
#     for i in range(0, len(string)-len(sub_string)+1):
#         if string[i] == sub_string[0]:
#             flag=1
#             for j in range (0, len(sub_string)):
#                 if string[i+j] != sub_string[j]:
#                     flag=0
#                     break
#             if flag==1:
#                 count += 1
#     return count



###################################


# # Complete the solve function below.
# def solve():
#
#
#     if __name__ == '__main__':
#         meal_cost = float(input())
#
#         tip_percent = int(input())
#         tip = meal_cost * (tip_percent / 100)
#
#         tax_percent = int(input())
#         tax = meal_cost * (tax_percent / 100)
#
#         return round(meal_cost + tip + tax)
#
# print(solve())




######################################################

# n=int(input())
#
# if n%2!=0:
#     print('Weird')
# else:
#     if n>=2 and n<5:
#         print('Not Weird')
#     elif n>=6 and n<=20:
#         print('Weird')
#     elif n>20:
#         print('Not Weird')



########################################################



# n=int(input())
#
# for i in range(1,11):
#     print(n,'*',i,'=',n*i)



###################################################


class Person:
    age=0
    def __init__(self, initialAge):

        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge


        # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self.age += 1

        # Increment the age of the person in herepg


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")







