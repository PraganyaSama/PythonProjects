# Program works on Caesar Script.

def printlist(l=list):
    string = ""
    for char in l:
        string += char
    return string


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet_lower = list("abcdefghijklmnopqrstyvwxyz")
alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
code_list = []

print(logo)
c = 0
while c == 0:
    a = input("Type 'encode' to encrypt. Type 'decode' to decrypt:- \n").casefold()
    if a == "encode":
        message = input("Enter your message: ")
        shift = int(input("Enter the shift number: "))
        for i in message:
            if i in alphabet_upper:
                index = alphabet_upper.index(i)
                if (index + shift) < 0:
                    index -= 26
                code_list.append(alphabet_upper[index + shift])
            elif i in alphabet_lower:
                index = alphabet_lower.index(i)
                if (index + shift) < 0:
                    index -= 26
                code_list.append(alphabet_lower[index + shift])
            else:
                code_list.append(i)
        a = printlist(code_list)
        print(f"Here's the encoded result: {a}")
    elif a == "decode":
        message = input("Enter your code: ")
        shift = int(input("Enter the shift number: "))
        for i in message:
            if i in alphabet_upper:
                index = alphabet_upper.index(i)
                if (index - shift) < 0:
                    index += 26
                code_list.append(alphabet_upper[index - shift])
            elif i in alphabet_lower:
                index = alphabet_lower.index(i)
                if (index - shift) < 0:
                    index += 26
                code_list.append(alphabet_lower[index - shift])
            else:
                print("Invalid")
                break
        a = printlist(code_list)
        print(f"Here's the decoded result: {a}")
    else:
        print("Invalid.")
    yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").casefold()
    if yes_no == "yes":
        continue
    elif yes_no == "no":
        break
    else:
        break
