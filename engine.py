import numpy as np

def count_threesome(color, board):

    count_r = 0
    count_c = 0

    sum_r = np.zeros((7, 1))
    sum_c = np.zeros((7, 1))

    for i in xrange(0, 7):
        if i != 3:
            for j in xrange(0, 7):
                if board[i, j] != 3:
                    if board[i, j] == color:
                        sum_r[i] += 1
            if sum_r[i] == 3:
                count_r += 1
        else:
            for j in xrange(0, 3):
                if board[i, j] == color:
                    sum_r[i] += 1
            if sum_r[i] == 3:
                count_r += 1
            sum_r[i] = 0
            for j in xrange(4, 7):
                if board[i, j] == color:
                    sum_r[i] += 1
            if sum_r[i] == 3:
                count_r += 1

    print "row 3s: "+str(count_r)

    for j in xrange(0, 7):
        if j != 3:
            for i in xrange(0, 7):
                if board[i, j] != 3:
                    if board[i, j] == color:
                        sum_c[j] += 1
            if sum_c[j] == 3:
                count_c += 1
        else:
            for i in xrange(0, 3):
                if board[i, j] == color:
                        sum_c[j] += 1
            if sum_c[j] == 3:
                count_c += 1
            sum_c[j] = 0
            for i in xrange(4, 7):
                if board[i, j] == color:
                    sum_c[j] += 1
            if sum_c[j] == 3:
                count_c += 1

    #print count_c
    total_threesome = count_r+count_c
    print "total threesomes: "+str(total_threesome)


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
        count_threesome(2, board)

    return rating

board = np.matrix([[2, 3, 3, 2, 3, 3, 2],
                   [3, 0, 3, 0, 3, 2, 3],
                   [3, 3, 0, 0, 1, 3, 3],
                   [2, 2, 2, 3, 2, 2, 2],
                   [3, 3, 0, 0, 1, 3, 3],
                   [3, 2, 3, 1, 3, 2, 3],
                   [0, 3, 3, 1, 3, 3, 0]])

evaluate(2, board)

