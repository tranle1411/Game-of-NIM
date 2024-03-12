### **README**

**Description:**
The program will play the Game of NIM with you.

**Game of NIM:**
The game starts with a pile of `n` number of sticks. Each turn, either you or the computer picks a maximum `x` of sticks away from the pile. Whoever picks the last stick wins.
Note: You choose `n` and `x`.

**Instruction:**
- [ ] 1. Download the folder
- [ ] 2. Run `main.py` in any Python Editor or IDE (ideally PyCharm or Visual Studio Code)
- [ ] 3. As the first prompt is printed, choose the total number of sticks you and the computer is going to play with (`0 < n`).
> Welcome to the Puzzle Game. Choose number level 1.very easy, or 2. easy, or 3. medium, or 4.hard, or 5.very hard:
> This is level ___ puzzle: _[insert the puzzle]_
- [ ] 4. As the next prompt is printed, choose a search method by typing down either 1 or 2
> Choose a search method 1. BFS or 2. Best First Search:
- [ ] 5. Wait for the program to run. Every states of the puzzle will be generated while looking for the final goal
- [ ] 6. When the program finish running, the number of nodes expanded and the number of moves will be shown

**File explanation:**
- `main.py` contains all prompts and inputs, as well as calling the search methods. Module used: `bfs `and `bestfirst`
- `BFS.py` contains the BFS (Breath First Search) search method. Modules used: copy, numpy, deque, and `helper`
- `BestFirst.py` contains the Best First Search search method. Modules used: copy, numpy, heapq, and `helper`
- `helper.py` contains `getGoal()` (get the Goal state), `swapPositions()` (swap the position of the '0' with another one), `print_array()` (print out the state), `find_empty()` (locate the '0'), and `find_h()` (calculate heuristic). Module used: copy
- `very_easy.txt` / `easy.txt` / `medium.txt` / `hard.txt` / `very_hard.txt`: contain each level of the puzzle problem
