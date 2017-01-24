import numpy as np


def count_3s(color, board):

    count_r = 0
    count_c = 0

    sum_r = np.zeros((7, 1))
    sum_c = np.zeros((7, 1))

    for i in xrange(0, 7):
        if i != 3:
            for j in xrange(0, 7):
                if board[i, j] == color:
                    sum_r[i] += 1
                if board[j, i] == color:
                    sum_c[i] += 1
            if sum_r[i] == 3:
                count_r += 1
            if sum_c[i] ==3:
                count_c += 1
        else:
            for j in xrange(0, 3):
                if board[i, j] == color:
                    sum_r[i] += 1
                if board[j, i] == color:
                    sum_c[i] += 1
            if sum_r[i] == 3:
                count_r += 1
            sum_r[i] = 0
            if sum_c[i] == 3:
                count_c += 1
            sum_c[i] = 0
            for j in xrange(4, 7):
                if board[i, j] == color:
                    sum_r[i] += 1
                if board[j, i] == color:
                    sum_c[i] += 1
            if sum_r[i] == 3:
                count_r += 1
            if sum_c[i] == 3:
                count_c += 1

    total_3s = count_r + count_c

    #print "row 3s: "+str(count_r)
    #print "column 3s: " + str(count_c)
    #print "total 3s: " + str(total_3s)

    return total_3s


def evaluate(player, board):

    rating = 0

    count1 = 0
    count2 = 0

    for i in xrange(0, 7):
        for j in xrange(0, 7):
           if board[i, j] == 1:
              count1 += 1
           if board[i, j] == 2:
              count2 += 1

    if count1 < 3:
        if player == 1:
            rating = -100
        else:
            rating = 100

    if count2 < 3:
       if player == 2:
            rating = -100
       else:
            rating = 100

    if rating != 100 and rating != -100:
        if player == 1:
            rating = 20*(count_3s(1, board)-count_3s(2, board))
        if player == 2:
            rating = 20*(count_3s(2, board)-count_3s(1, board))

    print "rating: " + str(rating)
    return rating

board = np.matrix([[0, 3, 3, 0, 3, 3, 0],
                   [3, 0, 3, 0, 3, 2, 3],
                   [3, 3, 0, 0, 1, 3, 3],
                   [0, 2, 2, 3, 1, 2, 0],
                   [3, 3, 0, 0, 1, 3, 3],
                   [3, 2, 3, 1, 3, 2, 3],
                   [0, 3, 3, 1, 3, 3, 0]])

evaluate(1, board)

