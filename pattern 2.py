for i in range(0,5):            # Rows k lie initialize - 0
    for j in range(0,5-i-1):    # 5-0-1=4 ...
        print(end=" ")          #  
    for j in range(0,i+1):      # 0,1 ...
        print("*",end=" ")
    print()
 
