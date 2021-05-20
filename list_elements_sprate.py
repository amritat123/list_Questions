def num(big_list):
    i = 0
    while i<len(big_list):
        small_list_length = len(big_list[i])
        i2 = 0
        while i2 <small_list_length:
            print (big_list[i][i2])
            i2 = i2 + 1
        i+=1
    print ("")
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
num(big_list)
