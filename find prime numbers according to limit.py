def is_prime_number(n:int)->int:
    """check wheather a number aprime or not """
    if not isinstance(n,int):
        raise TypeError("input must be a integer value")
    if n <=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

    # main execution
if __name__=="__main__":
    try:
        prime_number_list = []
        lower_limit = input("Enter your Lower Limit:")
        upper_limit = input ("input your Upper Limit: ")
        if not lower_limit.strip().isdigit():
            raise TypeError("lower limit must be valid integer")
        if not upper_limit.strip().isdigit():
            raise TypeError("upper limit must be a valid integer")
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)

        for i in range (lower_limit,upper_limit):
            if is_prime_number(i):
                # print(f"{i} prime number")
                prime_number_list.append(i)
        print(prime_number_list)
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)
        