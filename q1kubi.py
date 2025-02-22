
import sys
from collections import deque

def solve(pawn_col, pawn_row, knight_col, knight_row):
    """
    Finds the minimum number of moves for a knight to capture a pawn.

    Args:
        pawn_col (int): Pawn's column (1-8).
        pawn_row (int): Pawn's row (1-8).
        knight_col (int): Knight's column (1-8).
        knight_row (int): Knight's row (1-8).
    """

    if knight_col == pawn_col and knight_row == pawn_row:
        print(0)
        return

    q = deque([(knight_col, knight_row, 0)])
    visited = set()
    visited.add((knight_col, knight_row))

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    while q:
        col, row, dist = q.popleft()

        if col == pawn_col and row == pawn_row:
            print(dist)
            return

        for dc, dr in moves:
            new_col = col + dc
            new_row = row + dr

            if 1 <= new_col <= 8 and 1 <= new_row <= 8 and (new_col, new_row) not in visited:
                q.append((new_col, new_row, dist + 1))
                visited.add((new_col, new_row))


def in1move(pawnHor, pawnVer, knightHor, knightVer):
    if (((pawnHor - knightHor) == 2) or ((pawnHor - knightHor) == -2)):
        if ((pawnVer - knightVer == 1) or (pawnVer - knightVer == -1)):
            return 1
    if (((pawnVer - knightVer) == 2) or ((pawnVer - knightVer) == -2)):
        if ((pawnHor - knightHor == 1) or (pawnHor - knightHor == -1)):
            return 1
    return 0

def ustusteyanyana(pawnHor, pawnVer, knightHor, knightVer):
    if (((pawnHor - knightHor) == 0) and (((pawnVer - knightVer) == -1) or ((pawnVer - knightVer) == 1))):
        return 1
    if (((pawnVer - knightVer) == 0) and (((pawnHor - knightHor) == -1) or ((pawnHor - knightHor) == 1))):
        return 1
    return 0

def capraz(pawnHor, pawnVer, knightHor, knightVer):
    if(((pawnHor-knightHor == -1) or (pawnHor-knightHor == 1)) and (((pawnVer-knightVer == -1) or (pawnVer-knightVer == 1)))) :
        return 1
    return 0

def ikiustte(pawnHor, pawnVer, knightHor, knightVer):
    if((pawnHor - knightHor == 0) and  ((pawnVer - knightVer == 2) or (pawnVer - knightVer == -2))):
        return 1
    if ((pawnVer - knightVer == 0) and ((pawnHor - knightHor == 2) or (pawnHor - knightHor == -2))):
        return 1
    return 0

def ikicapraz(pawnHor, pawnVer, knightHor, knightVer):
    if(((pawnHor-knightHor == 2) or ((pawnHor-knightHor == -2))) and (((pawnVer-knightVer == 2)) or ((pawnVer-knightVer == -2)))):
        return 1
    return 0

def in0move(pawnHor, pawnVer, knightHor, knightVer):
    if ((pawnVer == knightVer) and (knightHor == pawnHor)):
        return 1
    return 0


def isin3(pawnHor, pawnVer, knightHor, knightVer):
    if -2 <= pawnHor - pawnVer <= 2 and -2 <= knightHor - knightVer <= 2:
        return 1
    else:
        return 0
def isedgecase(pawnHor, pawnVer, knightHor, knightVer):
    if((pawnHor == pawnVer == 1 and knightVer ==  knightHor == 2) or (pawnHor == pawnVer == 2 and knightVer ==  knightHor == 1)):
        return 1
    if ((pawnHor == 1 and pawnVer == 8 and knightVer == 7 and knightHor == 2) or (knightHor == 1 and knightVer == 8 and pawnVer == 7 and pawnHor == 2)):
        return 1
    if((pawnHor == pawnVer == 8 and knightVer ==  knightHor == 7) or (pawnHor == pawnVer == 7 and knightVer ==  knightHor == 8)):
        return 1
    if ((pawnHor == 8 and pawnVer == 1 and knightVer == 2 and knightHor == 7) or (knightHor == 8 and knightVer == 1 and pawnVer == 2 and pawnHor == 7)):
        return 1
    return 0

def harf_to_sayi(harf):
    """
    Harfi sayıya dönüştürür.

    Args:
        harf (str): Dönüştürülecek harf (a'dan h'ye).

    Returns:
        int: Dönüştürülmüş sayı (1'den 8'e). Eğer harf geçersizse, None döndürür.
    """
    harf_sozlugu = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }
    return harf_sozlugu.get(harf)  # Eğer harf bulunamazsa None döndürür


knighPos = input()
pawnPos = input()

pawnHor = harf_to_sayi(pawnPos[0])
pawnVer = int(pawnPos[1])
knightHor = harf_to_sayi(knighPos[0])
knightVer = int(knighPos[1])
test = isedgecase(pawnHor, pawnVer, knightHor, knightVer)
end = 0
if(test == 1):
    result = 4
    print(4)
    end = 1
if(end == 0):
    test = in0move(pawnHor, pawnVer, knightHor, knightVer)
    if(test == 1):
        result = 0
        print(0)
        end = 1
    if(end == 0):
        test = isin3(pawnHor, pawnVer, knightHor, knightVer)
        if(test == 1):
            if(in1move(pawnHor, pawnVer, knightHor, knightVer) == 1):
                result = 1
                print(1)
                end = 1
            if(end == 0):
                test2 = ustusteyanyana(pawnHor, pawnVer, knightHor, knightVer)
                if(test2 == 1):
                    result = 3
                    print(3)
                    end = 1
                if(end == 0):
                    test2 = capraz(pawnHor, pawnVer, knightHor, knightVer)
                    if(test2 == 1):
                        result = 2
                        print(2)
                        end = 1
                    if(end == 0):
                        test2 = ikicapraz(pawnHor, pawnVer, knightHor, knightVer)
                        if(test2 == 1):
                            result = 4
                            print(4)
                            end = 1

        if end == 0: # Move this to be aligned with "test = isin3..."
            test3 = solve(pawnHor, pawnVer, knightHor, knightVer)
