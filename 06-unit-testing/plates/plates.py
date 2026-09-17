"""

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if
meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#maximum 6 characters minimum 2
def is_two_six(s):
    #append strings to list
    list = []
    j = 0
    for char in s:
        list.append(char)
        j += 1
    if 1 < j < 7:
        return True
    else:
        return False

#is first two strings a letter
def first_two(s):
    list = []
    for char in s:
        list.append(char)
    if len(list) > 1:
        if list[0].isalpha() and list[1].isalpha():
            return True
        else:
            return False
    else:
        return False


#numbers must come at the end (3-6)
def number_end(s):
    list = []
    for char in s:
        list.append(char)
    for i in range(len(list)):
        if 2 < len(list) < 4: #for 3 chars
            if list[-1].isdigit(): # if last is digit return true
                    return True
            else:
                return False
        elif 3 < len(list) < 5: #for 4 chars
            if list[-2].isdigit(): # if 2nd last is digit make sure last is also digit
                if list[-1].isdigit():
                    return True
                else:
                    return False
            else:
                return True
        elif 4 < len(list) < 6: #for 5 characters
            if list[-3].isdigit(): #if 3rd last is digit make sure 2nd and last is digit
                if list[-2].isdigit() and list[-1].isdigit():
                    return True
                else:
                    return False
            elif list[-2].isdigit(): #if 2nd last is digit make sure last is digit
                if list[-1].isdigit():
                    return True
                else:
                    return False
            else:
                return True
        elif 5 < len(list) < 7: #for 6 chars
            if list[-4].isdigit(): #if char 3 is digit make sure 4,5,6 is digit
                if list[-3].isdigit() and list[-2].isdigit() and list[-1].isdigit():
                    return True
                else:
                    return False
            elif list[-3].isdigit(): #if char 4 is digit make sure 5,6 is digit
                if list[-2].isdigit() and list[-1].isdigit():
                    return True
                else:
                    return False
            elif list[-2].isdigit(): #if char 5 is digit make sure 6,7 is digit
                if list[-1].isdigit():
                    return True
                else:
                    return False

def no_digits(s):
    if s.isalpha():
        return True
    elif first_num(s) and number_end(s):
        return True
    else:
        return False

    #first number cannot be 0
def first_num(s):
    list = []
    for char in s:
        list.append(char)
        if 2 < len(list) < 4: #for 3 chars
            if list[-1].isdigit():
                if list[-1] != "0":
                    return True
                else:
                    return False
        if 3 < len(list) < 5: #for 4 chars
            if list[-2].isdigit():
                if list[-2] != "0":
                    return True
                else:
                    return False
            elif list[-1].isdigit():
                if list[-1] != "0":
                    return True
                else:
                    return False
        if 4 < len(list) < 6: #for 5 chars
            if list[-3].isdigit():
                if list[-3] != "0":
                    return True
                else:
                    return False
            elif list[-2].isdigit():
                if list[-2] != "0":
                   return True
                else:
                    return False
            elif list[-1].isdigit():
                if list[-1] != "0":
                    return True
                else:
                    return False
        if 5 < len(list) < 7: # for 6 chars
            if list[-4].isdigit():
                if list[-4] != "0":
                    return True
                else:
                    return False
            elif list[-3].isdigit():
                if list[-3] != "0":
                    return True
                else:
                    return False
            elif list[-2].isdigit():
                if list[-2] != "0":
                    return True
                else:
                    return False
            elif list[-1].isdigit():
                if list[-1] != "0":
                    return True
                else:
                    return False

    #no special characters
def spc_char(s):
    if s.isalnum():
        return True
    else:
        return False

def is_valid(s):
    #caps all characters
    s = s.upper()
    return is_two_six(s) and first_two(s) and no_digits(s) and spc_char(s)



if __name__ == "__main__":
    main()


