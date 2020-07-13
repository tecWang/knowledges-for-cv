for i in range(9):
    for j in range(i+1):
        print("{}*{}={}".format(j+1, i+1, (i+1)*(j+1)), end=" ")
    print("")