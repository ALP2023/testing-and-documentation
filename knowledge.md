### Reflection Questions for Portfolio Activity: ICTPRG443

1. **Debugging Methodology**: 
    - Outline the debugging methodology you employed to identify the bug(s) in the Tic-Tac-Toe game? What debugging tools did you use and how did they aid in the debugging process? 
    - My workflow begins with an initial visual run through of the code to identify issues and fix (where possible).
    - Then performing the following debugging process using the Pycharm debugging tool:
    - STEP1: Run the code
    - STEP2: Try to break it, identify an issue
    - STEP3: Review the Error(s) Raised
    - STEP4: Go to the code that raises the error
    - STEP5: Set break points by clicking in the left-hand margin next to the line of code where I want to start debugging. A red dot will appear, indicating a breakpoint.
    - STEP6: Run your Python script in debug mode (bug icon), then use the stepping controls to navigate through your code, inspect variables, and identify issues in your program. Inspect the values of variables by hovering over them in the code editor, also view them in the variables pane in the Debug tool window. 
    - STEP7: Once debugging is completed stop the debugging session by clicking the red square, remove breakpoints.
    - STEP8: Run the program again to check your fixes are correct. Rinse and repeat to seek another issue to resolve.

2. **Role of Documentation**: 
    - Did the existing documentation (comments, docstrings, onboarding documentation, etc.) help you in understanding and debugging the code? Provide examples.
The onboarding and readme documentation are particularly helpful, as it provide valuable information regarding the expectations of this assessment. The readme document, in particular, assisted in stepping through the processes for this assessment. However, the comments and docstrings tend to only have the basic information and could be expanded.

3. **Updating Documentation**: 
    - How did you go about updating the documentation? What information did you include to make the codebase easier to understand for future developers?
Updated doc strings using Google Doc style, which includes a short function description, the function's arguments (parameters), including their types and meanings, and specify the return value(s), including its type and meaning. For example, instead of simply commenting "Check rows for win conditions for a given player" for the _check_rows() function, using Google Doc style: 
    '''Check rows for win condition for a given player.
    Args:
      board(list): 3x3 grid to represent game board
      player(str): Checks for a win for player 'X' or 'O'

    Returns:
      bool: True if wins any row, else False

4. **Reflection on Testing**: 
    - How did writing test cases help you in the debugging process? Did the act of writing a test case provide any insights into the bug you were trying to fix?

5. **Testing Challenges and Strategies**: 
    - What challenges did you encounter while writing and running the test cases? What strategies did you employ to overcome these challenges?

6. **General Reflection**: 
    - How did this activity help you in understanding the importance of debugging, testing, and documentation in a real-world coding project? What are the key takeaways for you from this portfolio activity?

