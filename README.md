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
> Welcome to the game of NIM! Pick the total number of sticks (greater than 0): 
- [ ] 4. As the second prompt is printed, choose the maximum number of sticks can be picked each turn (`0 < x < n`).
> Good! Now pick the maximum number of sticks to pick each turn (between 0 and `n` "): 
- [ ] 5. The computer is going to play first. It will show the number of sticks it picks and the number of sticks left in the pile.
- [ ] 6. During your turn, enter the number of sticks you are going to pick (`x`).

**File explanation:**
- `main.py` contains all prompts and inputs, as well as calling the search methods. Module used: `bfs `and `bestfirst`
- `BFS.py` contains the BFS (Breath First Search) search method. Modules used: copy, numpy, deque, and `helper`
- `BestFirst.py` contains the Best First Search search method. Modules used: copy, numpy, heapq, and `helper`
- `helper.py` contains `getGoal()` (get the Goal state), `swapPositions()` (swap the position of the '0' with another one), `print_array()` (print out the state), `find_empty()` (locate the '0'), and `find_h()` (calculate heuristic). Module used: copy
- `very_easy.txt` / `easy.txt` / `medium.txt` / `hard.txt` / `very_hard.txt`: contain each level of the puzzle problem
