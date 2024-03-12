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
- Note: If you enter an invalid number of stick, you can choose again after this prompt:
> Invalid number! Pick again: 
- [ ] 5. The computer is going to play first. It will show the number of sticks it picks and the number of sticks left in the pile.
- [ ] 6. During your turn, enter the number of sticks you are going to pick (`x`).
- [ ] 7. After the last stick is picked, it will state the winner.

**File explanation:**
- `main.py` contains all prompts and inputs, as well as calling the Alpha-Beta method. Module used: `AlphaBeta`.
- `AlphaBeta.py` contains the Alpha-Beta algorithm and the Min-Max to find the game solution.
