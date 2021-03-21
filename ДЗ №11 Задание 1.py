for i in range(1, 7 + 1):

    for j in range(1, 7 + 1):

        if i % 2 == 0:

            if j % 2 == 0:

                print("***", end=' ')

            else:

                print('___', end=' ')

        else:

            if j % 2 != 0:

                print("***", end=' ')

            else:

                print('___', end=' ')

    print()
