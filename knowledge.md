### Reflection Questions for Portfolio Activity: ICTPRG443

1. **Debugging Methodology**: 
   Outline the debugging methodology you employed to identify the bug(s) in the Tic-Tac-Toe game? What debugging tools did you use and how did they aid in the debugging process? 
    - My workflow begins with an initial visual run through of the code to identify potential issues or problems.
    - Then perform the following debugging process using the Pycharm debugging tool:
    - STEP1: Run the code
    - STEP2: Try to break it, identify an issue
    - STEP3: Review the Error(s) Raised
    - STEP4: Go to the code that raises the error
    - STEP5: Set break points by clicking in the left-hand margin next to the line of code where I want to start debugging. A red dot will appear, indicating a breakpoint.
    - STEP6: Run your Python script in debug mode (bug icon), then use the stepping controls to navigate through your code, inspect variables, and identify issues in your program. Inspect the values of variables by hovering over them in the code editor, also view them in the variables pane in the Debug tool window. 
    - STEP7: Once debugging is completed stop the debugging session by clicking the red square, remove breakpoints.
    - STEP8: Run the program again to check your fixes are correct. Rinse and repeat to seek another issue to resolve.


2. **Role of Documentation**: 
    Did the existing documentation (comments, docstrings, onboarding documentation, etc.) help you in understanding and debugging the code? Provide examples.
   - The onboarding and readme documentation are particularly helpful, as it provide valuable information regarding the expectations of this assessment. The readme document, in particular, assisted in stepping through the processes for this assessment. However, the comments and docstrings tend to only have the basic information and could be expanded.


3. **Updating Documentation**: 
   How did you go about updating the documentation? What information did you include to make the codebase easier to understand for future developers?
    - I updated the doc strings using Google Doc style, which includes a short function description, the function's arguments (parameters), including their types and meanings, and specify the return value(s), including its type and meaning. 
    - For example, instead of simply commenting "Check rows for win conditions for a given player" for the _check_rows() function, using Google Doc style my comment would be: 
    
   '''Check rows for win condition for a given player.
    Args:
      board(list): 3x3 grid to represent game board
      player(str): Checks for a win for player 'X' or 'O'

    Returns:
      bool: True if wins any row, else False
    '''


4. **Reflection on Testing**: 
    How did writing test cases help you in the debugging process? Did the act of writing a test case provide any insights into the bug you were trying to fix?
    - Writing test cases helped with the debugging process, as it required one to think critically about how the code should behave, its functionality and limitations. This can lead to insights into the nature of the issue that requires to be fixed, as well as potential requirements to amend or improve the codebase.
    - A test case should isolate the specific functionality or feature where the issue occurs. Thus narrowing down the scope of the problem, making it easier to pinpoint the issue and avoid being overwhelmed by the complexity of the entire codebase.
    - Writing a test case that triggers the bug provides a clear and repeatable scenario to work with. It helps ensure that once the issue is fixed, it remains fixed because the test case will continue to pass.


5. **Testing Challenges and Strategies**: 
   What challenges did you encounter while writing and running the test cases? What strategies did you employ to overcome these challenges?
    - Writing tests is a skill that improves with practice. There's a distinct pattern in writing test cases, but understanding the nuances of what you're trying to test can be tricky and key to the process.  
    - My initial approach is to determine what exactly it is I want to test. For example, with the user input validation test, I'd approach it in the way I would during the code development stage, i.e. go through input iterations that could potentially break it.
    - In this assessment, we were dealing with legacy code. The strategy was to gradually introduce tests by focusing on areas with the highest risk or change frequency. Refactor and add tests as I go.
    - It was a real challenge to write tests handling exceptions and errors. It required writing different scenarios to check how the code handles different types of errors and exceptions by using specific test cases to provoke those errors.
    - It was also tricky to write clear and descriptive test names and comments, as what made sense to me might not to others. I'd used consistent testing patterns and conventions to make the tests easier (hopefully) to understand.
    - I kept the tests simple and focused on specific functionality, thus avoiding unnecessary complexity in the tests, which should make them easier to maintain.


6. **General Reflection**: 
   How did this activity help you in understanding the importance of debugging, testing, and documentation in a real-world coding project? What are the key takeaways for you from this portfolio activity?
    - Writing test cases is a structured and systematic approach to identifying, reproducing, and fixing issues.
    - Understanding what to test is key to writing successful test cases. Do this by breaking down the code into smaller parts and focus on testing the behavior of each component. Also, consider different scenarios, including valid and invalid inputs (as per issue 2 in my assessment).
    - Avoiding unnecessary complexity and creating clear setups and teardowns for the tests, i.e. set up the initial state, perform actions, and then assert the expected outcomes, should make them easier to understand and maintain.
    - Having comprehensive test cases provides some level of confidence that the code works as expected
    - Proper documentation makes the code and testcases more readable and helps developers understand how to use the functions and what functionality the tests cases are testing for.