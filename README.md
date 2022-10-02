# IntervalList
**By: Brian MacPherson (brimac1634@gmail.com)**

## Steps to install correct environment
- Navigate into the directory in the terminal
- Run "conda env create -f environment.yml"
- Run "conda activate intervallist"
- You can now test the project as mentioned below


## Test the project
**To test the project, run: "python test_interval_list.py"**

This runs automatic unit tests to validate the various methods that are included 
in the public interface of the IntervalList class (Testing is in line with the assignment).


## Notes
- If interval input was expected to be provided from user input, the assertions could be changed to try-except blocks for graceful error handling.
- Ideally, each unit test would test each class method individually for more isolated debugging, however, given the sequential nature of the tests given in the assignment, the testing class is running everything in two tests
- Assignment contained a mix of square brackets and parenthesis (ex: "// Should display: [1, 5) [10, 20)"). Since the instructions expect the class methods to receive lists, I assumed that the correct outputs should be all square brackets.
- Because the assignment instructions showed intervals being entered as lists, I have also used lists, however, I think tuples would be more fitting for this use case since tuples are faster and there is a fixed number of places in each interval.