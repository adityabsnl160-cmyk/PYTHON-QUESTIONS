def is_prime(n:int) -> bool:
    """ check whether a given number is a prime number or not.
    
    Args:
        n(int): The number to be checked .
        Returns:
            bool:
                True -> if the number is prime 
                False -> if the number is not prime 
        
        Raises :
            TypeError: if the input is not an integer
    """
    if not isinstance(n,int):
        raise TabError("input must be a integer value")
    if n <=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 
# ___MAIN__EXECUTION__
if __name__ == "__main__":
    num = int(input("Enter your number"))
    try:
        print(is_prime(num))
    except(TypeError,ValueError)as e:
        print(e)
    except Exception as e:
        print(e)