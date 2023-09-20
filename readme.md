[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2qFgZx4l)

# Portfolio Activity Handout: Debugging and Documentation in Intermediate Programming Techniques (ICTPRG443)

## Overview

The purpose of this portfolio activity is to evaluate your ability to debug code, write test cases, document your process, and use Git and GitHub effectively. This aligns with AQF Level 4 competency standards, specifically for the unit ICTPRG443.

This activity requires you to:

- Debug a provided buggy Tic-Tac-Toe game
- Use GitHub Issues for bug tracking
- Create branches locally and remotely on GitHub
- Write unit tests to cover identified issues
- Open and update Pull Requests (PRs)
- Update code and documentation
- Close GitHub issues through PRs

## Workflow

### 1. Debugging and Identifying Bugs

Use debugging techniques to identify bugs in the provided Tic-Tac-Toe game. This involves using both stand-alone debugging tools and IDE-based debugging features. Make sure to:

- Trace code execution
- Examine variable contents
- Use breakpoints as needed

### 2. Raise an Issue in GitHub Issues

Once a bug is identified:

- Go to the GitHub repository for this activity
- Navigate to the "Issues" tab
- Create a new issue, describing the bug in detail

### 3. Create a Local and Remote Branch

1. **Locally**: Create a new branch on your local machine to work on this issue. Name it appropriately.
    ```bash
    git checkout -b issue-<issue_number>
    ```
2. **Remotely**: Push the branch to the remote repository.
    ```bash
    git push -u origin issue-<issue_number>
    ```

### 4. Create a Test Case for the Issue

Write a unit test that exposes the bug. This test should fail initially because you have not yet fixed the bug.

### 5. Open a Pull Request (PR)

Open a PR for the new test case against the `main` branch. Ensure that your PR demonstrates that the build fails, which means your test case effectively captures the issue.

### 6. Fix the Code

Update the code to fix the bug. Run the test again locally to ensure it now passes.

### 7. Update the Documentation

Update any relevant comments, README files, or other documentation to reflect the changes you made to fix the bug.

### 8. Update the PR

Commit your code and documentation changes, and push them to the same branch.

### 9. Close the Issue

In your final commit message or PR description, include "fixes #\<issue_number\>" to indicate that this PR fixes the issue. Once the PR is merged, this will automatically close the corresponding issue.

### 10. Answer questions

Open `knowledge.md` and complete the short answer questions in that document. 

## Assessment Criteria

Your performance in this portfolio activity will be assessed based on the following:

- Effective use of debugging tools
- Quality and relevance of GitHub issues raised
- Proper branching strategy
- Quality of unit test cases
- Proper PR practices, including demonstrating initial failure and eventual success
- Quality of code fixes
- Adequacy and accuracy of documentation

