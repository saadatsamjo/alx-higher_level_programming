st_integer(my_list=[]):
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
