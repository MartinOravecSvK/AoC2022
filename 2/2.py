import sys
import os

games = {("A", "A"): (4, 4), ("A", "B"): (1, 8), ("A", "C"): (7, 3), 
         ("B", "B"): (5, 5), ("B", "C"): (2, 9), ("B", "A"): (8, 1),
         ("C", "C"): (6, 6), ("C", "A"): (3, 7), ("C", "B"): (9, 2)}

def round(tuple):
    return games[tuple]

def main():
    file = open(os.path.join(sys.path[0], "input"), "r")
    data = file.read().split("\n")
    file.close()

    sub_basic = {"X":"A", "Y":"B", "Z":"C"}

    # I taught it would be a bit more involved XD
    sub={"X": ["A", "B", "C", "A", "C", "B"],
         "Y": ["C", "A", "B", "B", "A", "C"],
         "Z": ["B", "C", "A", "C", "B", "A"]}
    results = []
    rel_results = []

    for i in range(0, 1):
        score_opp = 0
        score_me = 0
        for game in data:
            opp = game[0]
            me  = game[2]
            me = sub_basic[me][i]
            round_opp, round_me = round((opp, me))
            score_opp += round_opp
            score_me += round_me
        results.append((score_opp, score_me))
        rel_results.append(score_me-score_opp)
    
    print("Part one")
    print(results[0][1])

    sub_part2 = {("A", "X"):"C",
                 ("A", "Y"):"A",
                 ("A", "Z"):"B",
                 ("B", "X"):"A",
                 ("B", "Y"):"B",
                 ("B", "Z"):"C",
                 ("C", "X"):"B",
                 ("C", "Y"):"C",
                 ("C", "Z"):"A",}

    score_opp = 0
    score_me = 0
    for game in data:
        opp = game[0]
        me = sub_part2[(opp, game[2])]
        round_opp, round_me = round((opp, me))
        score_opp += round_opp
        score_me += round_me
    results.append((score_opp, score_me))
    rel_results.append(score_me-score_opp)

    print("Part two")
    print(results[1][1])

if __name__ == "__main__":
    main()