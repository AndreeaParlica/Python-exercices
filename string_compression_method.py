#implement a method that perform basic striing comprehension using the counts instead of repeted chars
#aaabbccccaaa -> a3,b2,c4,a3. if the string comprehension became smaller than the original string then you should return the original string

def string_com(string):
    items=[]
    last_char = ''
    char_count = 0
    for char in string:
        if char == last_char:
            char_count += 1
        else:
            if last_char != "":
                items.append(last_char+str(char_count))
            last_char = char
            char_count = 1
            
    items.append(last_char+str(char_count))
    compressed_str = "".join(items)
    
    if len(items) < len(string):
        return compressed_str
    else:
        return string
