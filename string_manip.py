if __name__ == '__main__':
    s = raw_input()
    
    alphanumeric = False
    
    for i in range(len(s)):
        if s[i].isalnum():
            alphanumeric = True
            
                
    if alphanumeric:
        for i in range(len(s)):
            if s[i].isdigit():
                alphanumeric = True
                
        print alphanumeric
    else:
        print False


    alphabetic = False

    for i in range(len(s)):
        if s[i].isalpha():
            alphabetic = True
            break

    if alphabetic:
        print True
    else:
	    print False

    digital = False

    for i in range(len(s)):
	    if s[i].isdigit():
		    digital = True
		    break


    if digital:
	    print True
    else:
	    print False

    hasLowerCase = False

    for i in range(len(s)):
	    if s[i].islower():
		    hasLowerCase = True
		    break

    if hasLowerCase:
	    print True
    else:
	    print False



    hasUpperCase = False

    for i in range(len(s)):
	    if s[i].isupper():
		    hasUpperCase = True
		    break

    if hasUpperCase:
	    print True
    else:
	    print False
    