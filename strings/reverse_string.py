def Reverse_String(String,res):
    for i in String:
        res = i + res
    return res

# Using Slicing

def Reverse_String_slicing(String):
    return String[::-1]