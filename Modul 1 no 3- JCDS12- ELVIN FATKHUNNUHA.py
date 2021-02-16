"""
Soal 3 - Ravelling & Knitting Words (40 Poin)
Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string

fungsi ravel(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :
def ravel(...):
    ......

    
    
# Use the function

print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))


# Output:
PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
DDiDigDigiDigitDigitaDigital
CCoCodCodiCodinCoding
SScSchSchoSchooSchool
Sedangkan fungsi knit(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :

def knit(...):
    ......
    
# Use the function

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))

# Output:

Purwadhika
Digital
Coding
School
"""
# No 3 Elvin Fatkhunnuha

def ravel(input_kata):
    list = []
    for i in range(len(input_kata), -1, -1):
        for j in range(0, len(input_kata)-i):
            list.append(input_kata[j])
    list = "".join(list)
    return list
            
    
input_kata = input("Masukkan kata untuk di ravel: ")  #Ravel words = not integer and not sentence
if input_kata.isdigit() or "." in input_kata or "," in input_kata:
    print("Invalid Input")
else:
    if input_kata.isalpha():
        print(ravel(input_kata))
    else:
        print("invalid Input")



def knit(input2):
    panjang_input2 = len(input2)
    tes3 = panjang_input2 - (input2.count(input2[0]))
    return input2[tes3:]



input2 = input("Masukkan kata untuk di knit: ")
if input2.isdigit() or "." in input2 or "," in input2:
    print("Invalid Input")
else:
    if input2.isalpha():
        print(knit(input2))
    else:
        print("invalid Input")






