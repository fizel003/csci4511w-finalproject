import sys
sys.path.append('aima-python')
from search import *
import math
import random
import time
import io
import sys
import re
import csv

def mhd(node):
    rows = 4
    columns = 2
    '''
    Define your manhattan-distance heuristic for the minigame here
    It should take in the current node, and return a numerical value.
    '''
    goals = {}

    for i in range(rows):
        for j in range(columns):
            goals[(i * columns) + j + 1] = [i, j]

    totaldistance = 0
    statetuple = node.state
    for i in range(len(statetuple) - 1):
        if statetuple[i] != 0:
            row_current = i // columns
            column_current = i % columns
            row_goal, column_goal = goals[statetuple[i]]

            distance = 0
            if column_current >= column_goal:
                if row_current != row_goal:
                    distance += (columns + 1)
                distance += (column_current - column_goal)
            else:
                distance += (column_current + (columns - column_goal) + 1)

            totaldistance += distance
    
    return totaldistance

class SurvivorsMinigameTest:

    def __init__(self):
        pass

    def test_problem(self):
        # Minigame example with A*
        # A 3x5 goal is (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
        #   which represents:   1  2  3  4  5
        #                  _    6  7  8  9  10
        #                       11 12 13 14 15
        #

        # In this example, we'll construct a puzzle with initial state
        #               1  2  3  4  5
        #         _     11 12 14 6  7
        #               9  10 13 8  15
        #
        # init = (2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 15, 11, 12, 13, 14, 0)
        init = (2, 5, 1, 6, 4, 3, 0)
        # init = (1, 2, 3, 4, 5, 11, 12, 14, 6, 7, 9, 10, 13, 8, 15, 0)
        # init = (15, 4, 6, 14, 3, 2, 8, 1, 12, 5, 10, 13, 9, 7, 11, 0)
        puzzle = SurvivorsMinigame(init)

        print("A* with Manhattan heuristic")
        start2x3 = time.time()
        print(astar_search(puzzle, mhd).solution())
        end2x3 = time.time()
        print("Elapsed time to solve a 2x3 solution with default heuristic: " + str(end2x3-start2x3))

    def test_problem_2(self):
        init = (2, 5, 1, 7, 6, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 4, 2)
        print("2x4 A* with default heuristic")
        start2x4 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end2x4 = time.time()
        print("Elapsed time to solve a 2x4 solution with default heuristic: " + str(end2x4-start2x4))
    
    def test_problem_3(self):
        init = (2, 5, 1, 7, 6, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 2, 4)
        print("4x2 A* with default heuristic")    
        start4x2 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end4x2 = time.time()
        print("Elapsed time to solve a 4x2 solution with default heuristic: " + str(end4x2-start4x2))

    def test_problem_4(self):
        init = (2, 9, 5, 1, 7, 6, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 3, 3)
        print("3x3 A* with default heuristic")    
        start3x3 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end3x3 = time.time()
        print("Elapsed time to solve a 3x3 solution with default heuristic: " + str(end3x3-start3x3))
    
    def test_problem_3x4(self):
        init = (2, 10, 9, 5, 1, 11, 12, 7, 6, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 3, 4)
        print("3x4 A* with default heuristic")    
        start3x3 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end3x3 = time.time()
        print("Elapsed time to solve a 3x4 solution with default heuristic: " + str(end3x3-start3x3))

    def test_problem_3x5(self):
        init = (2, 10, 9, 13, 14, 5, 1, 11, 12, 7, 6, 15, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 3, 5)
        print("3x5 A* with default heuristic")    
        start3x3 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end3x3 = time.time()
        print("Elapsed time to solve a 3x5 solution with default heuristic: " + str(end3x3-start3x3))
    
    def test_problem_8x2(self):
        init = (2, 10, 9, 13, 14, 5, 16, 1, 11, 12, 7, 6, 15, 4, 3, 8, 0)
        puzzle = SurvivorsMinigame(init, 8, 2)
        print("8x2 A* with default heuristic")    
        start3x3 = time.time()
        print(astar_search(puzzle, mhd, True).solution())
        end3x3 = time.time()
        print("Elapsed time to solve a 3x5 solution with default heuristic: " + str(end3x3-start3x3))
    
    def test_3x3s(self):
        times = []
        for i in range(20):
            list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 3, 3)
            print(f"3x3 A* with Manhattan heuristic: Trial {i+1}")    
            start3x3 = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            end3x3 = time.time()
            times.append(end3x3-start3x3)
        print(times)
    
    def test_3x4s(self):
        times = []
        for i in range(20):
            list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 3, 4)
            print(f"3x4 A* with Manhattan heuristic: Trial {i+1}")    
            start3x3 = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            end3x3 = time.time()
            times.append(end3x3-start3x3)
        print(times)

    def test_2x3s(self):
        individual_trials = []
        for i in range(50):
            list = [1, 2, 3, 4, 5, 6]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 2, 3)
            print()
            print(f"2x3 A* with Default heuristic: Trial {i+1}")    
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startdef = time.time()
            print(astar_search(puzzle, None, True).solution())
            enddef = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            defsol = astar_search(puzzle, None, True).solution()
            if match:
                expandeddef = int(match.group(1))
                frontierdef = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")

            print(f"2x3 A* with MHD heuristic: Trial {i+1}")   

            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startmhd = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            endmhd = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            mhdsol = astar_search(puzzle, mhd, True).solution()
            if match:
                expandedmhd = int(match.group(1))
                frontiermhd = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")
            individual_dict = {
                "input": input,
                "defSolution": defsol,
                "defExpanded": expandeddef,
                "defFrontier": frontierdef,
                "defTime": enddef-startdef,
                "mhdSolution": mhdsol,
                "mhdExpanded": expandedmhd,
                "mhdFrontier": frontiermhd,
                "mhdTime": endmhd-startmhd,
            }
            if(defsol == mhdsol):
                individual_dict["sameSolution"] = True
                individual_dict["betterSolution"] = "N/A"
            else:
                individual_dict["sameSolution"] = False
                individual_dict["betterSolution"] = "Manhattan" if len(mhdsol) < len(defsol) else "Default"

            print(individual_dict)
            individual_trials.append(individual_dict)
        
        with open('2x3output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=individual_trials[0].keys())
            writer.writeheader()
            writer.writerows(individual_trials)
    
    def test_3x2s(self):
        individual_trials = []
        for i in range(50):
            list = [1, 2, 3, 4, 5, 6]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 3, 2)
            print()
            print(f"3x2 A* with Default heuristic: Trial {i+1}")    
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startdef = time.time()
            print(astar_search(puzzle, None, True).solution())
            enddef = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            defsol = astar_search(puzzle, None, True).solution()
            if match:
                expandeddef = int(match.group(1))
                frontierdef = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")

            print(f"3x2 A* with MHD heuristic: Trial {i+1}")   

            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startmhd = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            endmhd = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            mhdsol = astar_search(puzzle, mhd, True).solution()
            if match:
                expandedmhd = int(match.group(1))
                frontiermhd = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")
            individual_dict = {
                "input": input,
                "defSolution": defsol,
                "defExpanded": expandeddef,
                "defFrontier": frontierdef,
                "defTime": enddef-startdef,
                "mhdSolution": mhdsol,
                "mhdExpanded": expandedmhd,
                "mhdFrontier": frontiermhd,
                "mhdTime": endmhd-startmhd,
            }
            if(defsol == mhdsol):
                individual_dict["sameSolution"] = True
                individual_dict["betterSolution"] = "N/A"
            else:
                individual_dict["sameSolution"] = False
                individual_dict["betterSolution"] = "Manhattan" if len(mhdsol) <= len(defsol) else "Default"

            print(individual_dict)
            individual_trials.append(individual_dict)
        
        with open('3x2output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=individual_trials[0].keys())
            writer.writeheader()
            writer.writerows(individual_trials)

    def test_2x3s(self):
        individual_trials = []
        for i in range(50):
            list = [1, 2, 3, 4, 5, 6]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 2, 3)
            print()
            print(f"2x3 A* with Default heuristic: Trial {i+1}")    
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startdef = time.time()
            print(astar_search(puzzle, None, True).solution())
            enddef = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            defsol = astar_search(puzzle, None, True).solution()
            if match:
                expandeddef = int(match.group(1))
                frontierdef = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")

            print(f"2x3 A* with MHD heuristic: Trial {i+1}")   

            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startmhd = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            endmhd = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            mhdsol = astar_search(puzzle, mhd, True).solution()
            if match:
                expandedmhd = int(match.group(1))
                frontiermhd = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")
            individual_dict = {
                "input": input,
                "defSolution": defsol,
                "defExpanded": expandeddef,
                "defFrontier": frontierdef,
                "defTime": enddef-startdef,
                "mhdSolution": mhdsol,
                "mhdExpanded": expandedmhd,
                "mhdFrontier": frontiermhd,
                "mhdTime": endmhd-startmhd,
            }
            if(defsol == mhdsol):
                individual_dict["sameSolution"] = True
                individual_dict["betterSolution"] = "N/A"
            else:
                individual_dict["sameSolution"] = False
                individual_dict["betterSolution"] = "Manhattan" if len(mhdsol) < len(defsol) else "Default"

            print(individual_dict)
            individual_trials.append(individual_dict)
        
        with open('2x3output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=individual_trials[0].keys())
            writer.writeheader()
            writer.writerows(individual_trials)
    
    def test_3x3s(self):
        individual_trials = []
        for i in range(50):
            list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 3, 3)
            # print()
            # print(f"3x3 A* with Default heuristic: Trial {i+1}")    
            
            # old_stdout = sys.stdout
            # sys.stdout = mystdout = io.StringIO()
            # startdef = time.time()
            # print(astar_search(puzzle, None, True).solution())
            # enddef = time.time()
            # sys.stdout = old_stdout
            # output = mystdout.getvalue()

            # match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            # defsol = astar_search(puzzle, None, True).solution()
            # if match:
            #     expandeddef = int(match.group(1))
            #     frontierdef = int(match.group(2))
            #     # print(f"Expanded: {expanded}, Frontier: {frontier}")
            # else:
            #     print("Could not parse output")

            print(f"3x2 A* with MHD heuristic: Trial {i+1}")   

            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startmhd = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            endmhd = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            mhdsol = astar_search(puzzle, mhd, True).solution()
            if match:
                expandedmhd = int(match.group(1))
                frontiermhd = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")
            individual_dict = {
                "input": input,
                # "defSolution": defsol,
                # "defExpanded": expandeddef,
                # "defFrontier": frontierdef,
                # "defTime": enddef-startdef,
                "mhdSolution": mhdsol,
                "mhdExpanded": expandedmhd,
                "mhdFrontier": frontiermhd,
                "mhdTime": endmhd-startmhd,
            }
            # if(defsol == mhdsol):
            #     individual_dict["sameSolution"] = True
            #     individual_dict["betterSolution"] = "N/A"
            # else:
            #     individual_dict["sameSolution"] = False
            #     individual_dict["betterSolution"] = "Manhattan" if len(mhdsol) <= len(defsol) else "Default"

            print(individual_dict)
            individual_trials.append(individual_dict)
        
        with open('3x3output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=individual_trials[0].keys())
            writer.writeheader()
            writer.writerows(individual_trials)

    def test_4x2s(self):
        individual_trials = []
        for i in range(50):
            list = [1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(list)
            input = tuple(list + [0])
            print(input)

            puzzle = SurvivorsMinigame(input, 4, 2)
            print()
            print(f"4x2 A* with Default heuristic: Trial {i+1}")    
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startdef = time.time()
            print(astar_search(puzzle, None, True).solution())
            enddef = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            defsol = astar_search(puzzle, None, True).solution()
            if match:
                expandeddef = int(match.group(1))
                frontierdef = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")

            print(f"4x2 A* with MHD heuristic: Trial {i+1}")   

            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            startmhd = time.time()
            print(astar_search(puzzle, mhd, True).solution())
            endmhd = time.time()
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            

            match = re.search(r'(\d+)\s+paths have been expanded and\s+(\d+)\s+paths remain in the frontier', output)
            mhdsol = astar_search(puzzle, mhd, True).solution()
            if match:
                expandedmhd = int(match.group(1))
                frontiermhd = int(match.group(2))
                # print(f"Expanded: {expanded}, Frontier: {frontier}")
            else:
                print("Could not parse output")
            individual_dict = {
                "input": input,
                "defSolution": defsol,
                "defExpanded": expandeddef,
                "defFrontier": frontierdef,
                "defTime": enddef-startdef,
                "mhdSolution": mhdsol,
                "mhdExpanded": expandedmhd,
                "mhdFrontier": frontiermhd,
                "mhdTime": endmhd-startmhd,
            }
            if(defsol == mhdsol):
                individual_dict["sameSolution"] = True
                individual_dict["betterSolution"] = "N/A"
            else:
                individual_dict["sameSolution"] = False
                individual_dict["betterSolution"] = "Manhattan" if len(mhdsol) <= len(defsol) else "Default"

            print(individual_dict)
            individual_trials.append(individual_dict)
        
        with open('5x2output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=individual_trials[0].keys())
            writer.writeheader()
            writer.writerows(individual_trials)



def main():
    
    minigame = SurvivorsMinigameTest()
 
    # rows x columns

    #=======================
    # print('Test Problem 2x3 result:')
    # print('=======================')
    # minigame.test_problem()

    # print('Testing 20 2x3s result:')
    # print('=======================')
    # minigame.test_2x3s()

    print('Testing 50 3x2s result:')
    print('=======================')
    minigame.test_3x2s()

    # print('Testing 50 3x3s result:')
    # print('=======================')
    # minigame.test_3x3s()

    # print('Testing 50 4x2s result:')
    # print('=======================')
    # minigame.test_4x2s()

    
if __name__ == '__main__':
    main()
