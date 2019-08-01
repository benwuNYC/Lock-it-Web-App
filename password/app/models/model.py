def check_password(string):
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "`", "~", ":", "/", ".", "?", ",", "<", ">", "+", "="]
    print(string)
    print(len(string))
    if (not string.islower()) and (not string.isupper()) and (len(string) > 8) and (not string.isalpha()):
        for char in special_chars:
            print("in for")
            if string.find(char) != -1:
                return True
    
        
    return False