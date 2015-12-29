def anti_vowel(text):
    return_string = ""
    for char in range(len(text)):
        if check_if_vowel(char) == False:
            return_string = char
        
            
    return return_string
    
def check_if_vowel(char):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
    
    for i in vowels:
        if char == vowels[i]:
            return True
        else:
            return False
    
            
