from fastapi import FastAPI, Request

app = FastAPI(title="Tic-Tac-Toe")

@app.get("/")
def api_read_root():
    return {"msg": "Welcome to a poor implementation of Tic-Tac-Toe using FastAPI!"}

def reset(s):
    s.board = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    s.gameState = 'play'
    s.player = 'O'
reset(app.state)

def nextPlayer(s):
    s.player = 'X' if s.player == 'O' else 'O'
    return s.player

#def ppBoard(s):
#    r = ""
#    for r in s.board:
#        for x in r:
#            r.append(f"{x}|")
#        r.append("------\n")
#    return r

@app.put("/reset")
def api_reset(request: Request):
    reset(request.app.state)

@app.put("/place/{x}_{y}")
def api_place(x: int, y: int, request: Request):
    s = request.app.state
    if s.gameState != 'play':
        return {'s.board' : s.board, 'error' : 'game ended'}
    if x not in range(0, 3) or y not in range(0, 3):
        return {'s.board' : s.board, 'error' : 'invalid move: coordinates are not in the range [0;2]'}
    if s.board[x][y] != ' ':
        return {'s.board' : s.board, 'error' : f"invalid move: s.board[{x}][{y}] is not empty"}
    s.board[x][y] = nextPlayer(s)
    if checkVictory(s):
        s.gameState = 'end'
        return {'s.board' : s.board, 'msg' : f"{s.player} won!"}
    if checkStalemate(s):
        s.gameState = 'end'
        return {'s.board' : s.board, 'msg' : f"stalemate"}
    return {'s.board' : s.board, 'msg' : f"placed {s.player} at s.board[{x}][{y}]"}

def checkStalemate(s):
    for r in s.board:
        for x in r:
            if x == ' ':
                return False
    return True

def checkVictory(s):
    def check(cells):
        if all([i=='O' for i in cells]) or all([i=='X' for i in cells]):
            s.gameState = 'win'
    # прямые по горизонтали
    for y in (0,1,2):
        check([s.board[x][y] for x in (0,1,2)])
    # прямые по вертикали
    for x in (0,1,2):
        check([s.board[x][y] for y in (0,1,2)])
    # диагональ сверху-слева вправо-вниз
    check([s.board[x][y] for x, y in ((0,0), (1,1), (2,2))])
    # диагональ справа-сверху влево-вниз
    check([s.board[x][y] for x, y in ((2,0), (1,1), (0,2))])
    return s.gameState == 'win'
