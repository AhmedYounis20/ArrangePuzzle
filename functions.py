def possibleMoves(Puzzle):
    EmptyCellIndex=Puzzle.index(0);
    result=[]
    if (EmptyCellIndex<=5): result+=['^'];
    if (EmptyCellIndex%3<2): result+=["<"];
    if (EmptyCellIndex>=3): result+=['V'];
    if (EmptyCellIndex%3>0): result+=[">"];
    return result;

def Move(Puzzle , Selected_Move):
    # 3,1,2,
	# 4,0,5,
	# 6,7,8
    EmptyCellIndex=Puzzle.index(0);
    if (Selected_Move=="V"):
        Puzzle[EmptyCellIndex],Puzzle[EmptyCellIndex-3]=Puzzle[EmptyCellIndex-3],Puzzle[EmptyCellIndex];
    elif (Selected_Move=="^"):
        Puzzle[EmptyCellIndex],Puzzle[EmptyCellIndex+3]=Puzzle[EmptyCellIndex+3],Puzzle[EmptyCellIndex];
    elif (Selected_Move==">"):
        Puzzle[EmptyCellIndex],Puzzle[EmptyCellIndex-1]=Puzzle[EmptyCellIndex-1],Puzzle[EmptyCellIndex];
    elif (Selected_Move=="<"):
        Puzzle[EmptyCellIndex],Puzzle[EmptyCellIndex+1]=Puzzle[EmptyCellIndex+1],Puzzle[EmptyCellIndex];
    return Puzzle;

def checkWinning(Puzzle):
    for i in range(len(Puzzle)):
        if (i!= Puzzle[i]): return 0;

    return 1;
