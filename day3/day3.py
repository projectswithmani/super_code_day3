# paired output

# problem statement : for each number in list_b ,
# get the number and its position(index)
# in mylist as areturn list of tuples.

# mylist = [9,3,6,1,5,0,2,4,7,]
# list_b = [6,4,6,1,2,20]
# result=[(6,2),(4,8)]
mylist= [9,3,6,1,5,0,2,4,7]
list_b = [6,4,6,1,2,2]
result=[]
for i in list_b:
     for j in mylist:
          if (i==j):
               result.append((i,mylist.index(j)))
print(result)
#another 
     
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
print([(i,mylist.index(i)) for i in list_b])

#using Dict

dict1={}
for i in list_b:
    dict1[i] = mylist.index(i)
print(dict1)



###################################################################################################################################################
# problem statement: the goal is to tokenize the following 5 sentences into words, excluding the stop words

# input:
# sentences = [ " a new world recod was set",
#              "in the eve of diwali of ayodhya",
#              "with over three lakh diya or earthen lamps",
#              "lit up simultaneously on the banks of the sarayu river"
     
# ]

# stopwords = [ 'for','a','of','the','and', 'to', ' in' , 'on', 'with' , 'was']

sentences = [ " a new world recod was set",
              "in the eve of diwali of ayodhya",
              "with over three lakh diya or earthen lamps",
              "lit up simultaneously on the banks of the sarayu river"
     
 ]
stopwords = [ 'for','a','of','the','and', 'to', ' in' , 'on', 'with' , 'was']
result=[]

for sentence in sentences:
    row_data=[]
    for  words in sentence.split():
        if words not in stopwords:
            row_data.append(words)
    result.append(row_data)
print(result)

#################################################################################################################################################
# input: a string of a comma separated numbers. the number 5 and 8 are present in the list. assumee that 8 always comes after 5.
# case1: num1 = add LL THE NUMBER which do not lue between 5 and 8 in the input 
# case 2:num2 = number formed by concatenating all numbers from 5 to 8
# otput sum of num1 and num2

# ex
# 3,2,6,5,1,4,8,9

# num1 = 3+2+6+9=20
# num2 = 5148

# o/p = 5148+20 = 5168
# # # ##########################################################################################################################################
array =[3,2,6,5,1,4,8,9]
number1 = sum(array[0:array.index(5)] + array[array.index(8)+1:])
l = array[array.index(5):array.index(8)+1]
number2 = ""
for i in l:
    number2+=str(i)
print(array)
print(int(number1))
print(int(number2))
print(int(number2)+number1)



####################################################################################
# string rotation
# input : rhdt : 246, ghftd:1246
# exp1: here the sgtring is associated with thr numbersep by :
# --> if sum of squares of digit is even  then rotatew the string  by 1 position
# --> if sum of squares of digit is odd then rotatew the string left by 2 position
# 2*2+4*4+6=57 which is odd so rotate left by 2 : ghftd = ftdgh

s=input().split(",")  #rhdt:246,ghftd:1246
stt=[]
numm = []
for i in s:
    s1,n=i.split(": ")
    stt.append(s1) #stt = [rhdt],ghftd
    numm.append(n) #numm=[246,1246]
def rotate (ss,n):
    n= str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss [-1]+ss[:-1]
    else:
        return ss[2:] + ss[:2]
for i in range(len(numm)):

    print(rotate(stt[i],numm[i]))


###################################################################################################

# given a number n,write a program to find the sum of the larghest prime factor of 
# each of nine consecutive numbers startinng from n

# g(n) = f(n)+ f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+6) + f(n+7) + f(n+8)
# where g(2) is the sum and f(n) is the largest prime factor of n
# for example ,
# g(10)=f(10)+f(11)+ f(12)+ f(13)+ f(14)+ f(15)+ f(16)+ f(17)+ f(18)
#     = 5    +  11  +  3 +  13   +   7   +  5   +  2  +   17   + 3
#     =66 



array  = []
array = int (input())
print(array)










