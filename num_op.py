import re

def get_num(txt):
   
    num = re.findall(r'\d+', txt) 
    num = [int(num) for num in num]
    return num[0] if num else None



