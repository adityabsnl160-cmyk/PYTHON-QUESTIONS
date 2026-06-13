def rev_string(string:str)->str:
    """Function to do reverse of given string"""
    if not isinstance(text,str):
        raise TypeError("input should be string")
        if text=="":
            raise ValueError("input cannot be empty")
    rev=""
    for char in text:
        rev=char+rev
    return rev
    
# __MAIN__EXECUTION__
if __name__ == "__main__":
    text = "Hello Python"
    try:
        print(rev_string(text))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)
        