# 🐲 DnD and Probability 🎲
In Dungeons & Dragons (DnD), some dice rolls are made with advantage or disadvantage. Rolling with advantage means rolling two dice instead of one and keeping the highest result. Conversely, rolling with disadvantage means rolling two dice and taking the lowest result. Does that make sense? Let’s dive in!

# Instructions 📝
Below are several problems that you need to submit as `.py` files in the repository. Each problem is numbered, and you should **submit one file per problem**. Use `problem1.py` for problem 1, use `problem2.py` for problem 2 and continue this pattern for all problems.  

## General Instructions
- **Code Documentation** 💻: Ensure that you document your code wherever it's necessary to explain logic or clarify steps.
- **Mathematical Proof Requirement** 𝞹: Any non-trivial mathematical concept or tool you use to solve a problem must be proven and clearly linked to the problem at hand. If you use a tool without explaining it **and** providing a correlation to the problem, it will result in no marks.
- **Output Format**: Your program should print **only** the required result. For example:
  - Correct: `0`
  - Incorrect: `The answer is 0`
- **Input Assumptions**: If the problem specifies any input, you can assume that the input will be given in the expected format (correct data type and order). Therefore, you can directly use `input()` to receive those values without further validation.
## Specific Instructions 
- **No Python Libraries Allowed**: For this assignment, do not use any external Python libraries or modules. Write the solution purely in basic Python. 😈
 **Strategy** 🧠: If you're feeling confident 🤓, it's a good idea to tackle the most challenging problem first, and then work your way backward to the simpler ones.

# Problems 🛠️

## Problem 1
Suppose you have disadvantage and you throw 2d20 (2 dice with 20 faces). What is the expected value of this roll?

## Problem 2
Suppose you have advantage and you throw 2d20 (2 dice with 20 faces). What is the expected value of this roll?

## Problem 3
Suppose you have advantage and you throw 4d20 (4 dice with 20 faces). What is the expected value of this roll?

## Problem 4
Suppose you have advantage and you throw 4d100 (4 dice with 100 faces). What is the expected value of this roll?

## Problem 5
Suppose you roll $n$ dice with $m$ faces (where these parameters are provided as input, first $n$, then $m$), and you are playing with disadvantage/advantage, represented by a boolean variable called `adv`, which is `True` for advantage and `False` for disadvantage.
- Write a code that provides the expected value of the number you would get. You will receive as inputs  $n$, $m$ and `adv` as a string: `"(n,m,adv)"`.
- What would happen if $n \to \infty$? 
- What would happen if $m \to \infty$? 

