def mult_table(N,M):
    for i in range(N,M+1,1):
        for j in range(1,13,1):
            print('{} x {} = {}'.format(i,j,i*j))


mult_table(2,7)
