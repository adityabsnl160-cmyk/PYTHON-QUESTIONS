def largest_number(lst:list)->int:
    """function to find largest number in the given list"""
    if not isinstance(lst,list):
        raise TypeError("input should be a list")
    if lst == []:
        raise ValueError("input cannot be empty")
    i = 0
    largest = lst[0]
    while i<len(lst):
        if lst[i] > largest:
            largest = lst[i]
        i += 1
    return largest

# __MAIN__EXECUTION__
if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9,10]
    try:
        print(largest_number(lst))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)