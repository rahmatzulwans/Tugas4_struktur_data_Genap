print ("NAMA  : RAHMAT ZULWAN S")
print ("NIM   : E1E1 19 010")
print ("KELAS : GENAP")
print ("   ")
print ("   ")


class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack kosong")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack kosong")
        return self._data.pop()

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()

    ofile = open(filename, "r")
    k = ofile.readlines()
    for i in k:
        print(i.rstrip())

def is_matched(expr):
    lefty = "({[" 
    righty = ")}]" 
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) 
        elif c in righty:
            if S.is_empty():
                return False 
            if righty.index(c) != lefty.index(S.pop()):
                return False 
    return S.is_empty()

loopingStart = True

while loopingStart :
    print("\nPilihan :")
    print("1. Reverse File \n 2. Matching Delimiters \n 3. Keluar")
    a = int(input("Masukkan Pilihan Kamu : "))
    if a == 1 :
        namaFile = input("Masukkan File Kamu : ")
        print(namaFile + ".txt")
        reverse_file(namaFile + ".txt")
    elif a == 2 :
        expression = input("Masukkan Expression : ")
        cocok = is_matched(expression)
        if cocok:
            print("\nSemua delimiters cocok")
        else :
            print("\nTerdapat delimiters yang tidak cocok")
    else :
        break
