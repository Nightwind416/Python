testBoard = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
'5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

boardGrid = {'1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
             '2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
             '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
             '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
             '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
             '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
             '7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
             '8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '',}
pieceList = {'wpawn': 0, 'wknight': 0,'wbishop': 0,'wrook': 0,'wqueen': 0,'wking': 1,
             'bpawn': 0, 'bknight': 0,'bbishop': 0,'brook': 0,'bqueen': 0,'bking': 1, '': 0}


def isValidChessBoard(board):
    #   check valid spaces
    for key in board:
        if key not in boardGrid:
            print('Piece outside board limits')
            break
        else:
#             print('Piece within board limits')
            continue
    #   check valid pieces
    for value in board.values():
        if value not in pieceList:
            print('Incorrect piece type')
#             break
            continue
        else:
#             print('Correct piece type')
            continue
    #   check piece count valid
    pieceCount = {}
    for key, value in board.items():
        pieceCount = pieceCount + board.get(value, 0)
        print('Piece count: ' + str(pieceCount))
    return pieceCount

isValidChessBoard(testBoard)