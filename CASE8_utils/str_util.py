#String related tool module

def str_reverse(s):
    """
    Inversion string
    :param s:The string to be reversed
    :return:The string after inversion
    """
    return s[::-1]

def substr(s,x,y):
    """
    Completes slicing the given string with the given subscript
    :param s:The sliced string
    :param x:The beginning subscript of the slice
    :param y:The ending subscript of the slice
    :return:Sliced string
    """
    return s[x:y:1]

if __name__ == '__main__':
    print(str_reverse("Avemujica"))
    print(substr("Mygo", 1, 3))
