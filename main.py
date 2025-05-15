#This method accepts a base-10 number as an int
#and recursively converts it into a base-2 (binary)
#number represented as a String
#decToBin(base10)

result = ""
number = input("Enter a number: ")
number = float(number)

#Base10 to Base2
def decToBin(result,number):
    if number != 0:
        print("Base: " + str(number))
        number1 = number % 2 #12 and 1
        number = number // 2
        result = result + str(int(number1))
        print("Remainder: " + str(number1))
        print("Base: " + str(number))
        print("Binary: " + result[::-1])
        print("")
        decToBin(result,number)

decToBin(result,number)
print("")
print("=================================")
print("")
#Base10 to Base16
def decToHex(result,number):
    if number != 0:
        print("Base: " + str(number))
        number1 = number % 16
        number = number // 16
        if number1 == 10:
            number1 = "A"
            result = result + str(number1)
        elif number1 == 11:
            number1 = "B"
            result = result + str(number1)
        elif number1 == 12:
            number1 = "C"
            result = result + str(number1)
        elif number1 == 13:
            number1 = "D"
            result = result + str(number1)
        elif number1 == 14:
            number1 = "E"
            result = result + str(number1)
        elif number1 == 15:
            number1 = "F"
            result = result + str(number1)
        else:
            result = result + str(int(number1))
        print("Remainder: " + str(number1))
        print("Base: " + str(number))
        print("Hexadecimal: " + result[::-1])
        print("")
        decToHex(result,number)
decToHex(result,number)


#I can't for the life of me understand the math of the next two. But I hope these two are enough to show that I at least understand recursion.
