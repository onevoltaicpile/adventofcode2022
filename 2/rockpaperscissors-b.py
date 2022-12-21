import os
import sys

def translatePlayerAction(playerAction):
    match playerAction:
        case 'A':
            return 'Rock'
        case 'B':
            return 'Paper'
        case 'C':
            return 'Scissors'
        case _:
            return 'Err'

def translateIntendedResult(intendedResult):
    match intendedResult:
        case 'X':
            return 'lose'
        case 'Y':
            return 'draw'
        case 'Z':
            return 'win'
        case _:
            return ''

def calculatePlayer2Action(player1, intendedResult):
    if intendedResult == 'draw':
        return player1
    elif intendedResult == 'lose':
        match player1:
            case 'Rock':
                return 'Scissors'
            case 'Paper':
                return 'Rock'
            case 'Scissors':
                return 'Paper'
            case _:
                return ''
    else:
        match player1:
            case 'Rock':
                return 'Paper'
            case 'Paper':
                return 'Scissors'
            case 'Scissors':
                return 'Rock'
            case _:
                return ''

def determineRoundWinner(o,r):
    if player1 == player2:
        return 'draw'
    elif player1 == 'Rock':
        if player2 == 'Paper':
            return 'player2'
        return 'player1'
    elif player1 == 'Paper':
        if player2 == 'Scissors':
            return 'player2'
        return 'player1'
    elif player1 == 'Scissors':
        if player2 == 'Rock':
            return 'player2'
        return 'player1'       

def calculateScore(player, roundWinner, playerAction):
    match playerAction:
        case 'Rock':
            score = 1
        case 'Paper':
            score = 2
        case 'Scissors':
            score = 3
        case _:
            score = 0
    if roundWinner == 'draw':
        score += 3
    elif player==roundWinner:
        score += 6
    return score

def determineRoundScore(o,r):
    roundWinner = determineRoundWinner(o,r)
    player1Score = calculateScore('player1',roundWinner,o)
    player2Score = calculateScore('player2',roundWinner,r)
    return [player1Score,player2Score]

with open(os.path.join(sys.path[0], 'input.txt'), 'r') as file:
    player1Scores = []
    player2Scores = []
    for line in file:
        round = line.strip().split(' ')
        player1 = translatePlayerAction(round[0])
        intendedResult = translateIntendedResult(round[1])
        player2 = calculatePlayer2Action(player1,intendedResult)
        roundResult = determineRoundScore(player1,player2)
        player1Scores.append(roundResult[0])
        player2Scores.append(roundResult[1])
    player2FinalScore = sum(player2Scores)
    print(player2FinalScore)