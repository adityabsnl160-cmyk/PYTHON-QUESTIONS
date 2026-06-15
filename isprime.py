def is__prime__(n:int)->bool:
    """docstring"""
    if not isinstance(n,int):
        raise TypeError("input must be integer value")
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

# Manin__Execution
if __name__=="__main__":
    num = int(input("Enter a number"))
    try:
        print(isprime(num))
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    
    