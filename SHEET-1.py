#1


#2


print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=30; print(a)
print(True*False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print(False in 'False')
print(((True == False) or (False > True)) and (False <= True))


#3


s1 = "Nice to have it"
s2 = "here"
print(s1,s2)


#4


a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])


#5


a.insert(0,s1)
a.append(s2)
print(a)


#6


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

for i in numbers:
    if i < 238 and i%2==0:
        print(i)


#7


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))


#8


string = input('Enter a string: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = string.lower()
flag = 0
for i in alphabet:
    if i not in string:
        flag = 1
        break
if flag == 1:
    print('False')
else:
    print("True")


#9


n=int(input('Enter the value of n:' ))
num1 = str(n)
num2 = num1 + num1
num3 = num2 + num1
print(int(num1) + int(num2) + int(num3))


#10


inp = input('Enter the list: ')
inp = inp.split('#')
u = inp[0].split()
v = inp[1].split()
x = []
y = []
for i in u:
    x.append(int(i))
for i in v:
    y.append(int(i))
print('X = ',x)
print('Y = ',y)


#11


l = input('Enter the list of words: ')
lst = l.split(',')
print(','.join(sorted(list(set(lst)))))


#12


d = {'Student':['Rahul','Kishore','Vidhya','Raakhi'] , 'Marks':[57,87,67,79]}
max = max(d.get('Marks'))
i = d.get('Marks').index(max)
print(d.get('Student')[i])


#13


s5=input("Enter a string:")
l=0
d=0
for i in s5:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)


#14


d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)
