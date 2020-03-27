import collections

def ValidChessBoard(chessboard):
    Bcounter = 0
    Wcounter = 0
    flag = 'no'
    piece_checker = collections.Counter()
    location_checker = collections.Counter()
    pieces = ['bking','wking','bqueen','wqueen','bbishop','wbishop','bknight','wknight','brook','wrook','bpawn','wpawn']

    try:
        #checking if the names of all the pieces are valid
        if all(value in pieces for value in chessboard.values()) and \
        all((int(key[0:-1]) > 0 and int(key[0:-1]) < 10) for key in chessboard.keys()):

            #counting the number of pieces each player has
            for value in chessboard.values():
                if value.startswith('w'):
                    Wcounter += 1
                elif value.startswith('b'):
                    Bcounter +=1
            if Bcounter > 16 or Wcounter > 16:
                print('One of your players has too many pieces')
                return False

            #counting up the total values of each specific piece
            for value in chessboard.values():
                piece_checker[value]+=1

            #checking if players' have too many pieces
            for key, value in piece_checker.items():
                if (key == 'bking' or key == 'wking' or key == 'bqueen' or key == 'wqueen') and value > 1:
                    print('You have too many ' + key + ' pieces. It should only be 1 piece.')
                    return False
                elif (key == 'bbishop' or key == 'wbishop' or key == 'bknight' or key == 'wknight' \
                or key == 'brook' or key == 'wrook') and value > 2:
                    print('You have too many ' + key + ' pieces. It should only be 1 piece')
                    return False
                elif (key == 'bpawn' or key == 'wpawn') and value > 8:
                    print('You have too many ' + key + ' pieces. It should only be 1 piece')
                    return False

            #second check: if any keys contain letters other than a, b, c, d, e, f, g, h, then it is not valid location and return false
            if any(key[-1] not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') for key in chessboard.keys()):
                print('One of your pieces is not in a valid location. Please choose a new location.')
                return False

        else:
            print('Incorrectly named pieces and/or locations')
            return False

    except ValueError:
        print('First part of the location must be a number')
        return False

ValidChessBoard({'1c': 'wrook', '1b': 'wrook'})