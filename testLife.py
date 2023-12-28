import life
testDeadState = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]

testState = [[0,1,0],
             [1,0,0],
            [0,1,0]]

testState_nextState = [[0,0,0],
                       [1,1,0],
                       [0,0,0]]

def createTestBoard():
    return life.createBoard(3,3)

def test_CreateBoard():
    board = createTestBoard()
    assert len(board) == 3
    assert len(board[0]) == 3
    assert board==testDeadState
    print("testCreateBoard passed")

def test_getNeighbors():
    neighbours = life.getNeighbours(0,0,testState)
    assert(neighbours == 2)
    neighbours2 = life.getNeighbours(0,1,testState)
    assert(neighbours2 == 1)
    print("test_getNeighbors passed")

def test_nextState():
    board = life.nextState(testState)
    assert(board == testState_nextState)    
    print("Next state passed")

if __name__ == "__main__":
    test_CreateBoard()
    test_getNeighbors()
    test_nextState()
