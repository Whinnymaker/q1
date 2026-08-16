# q1_sg2_a2
Annex C
# Code Quality Assessment Worksheet

Section: PINATUBO Score:____________

C#4,5,6 / Name: ESDRELON, DUCUSIN, DE LEON Date: 8/16/2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

PseudoCode 2

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm



Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- Pseudocode 1 is faster because it uses only one loop, while Pseudocode 2 uses two nested loops. Pseudocode 1 checks each number only once, making it more efficient for a very large list. Pseudocode 2 repeatedly compares numbers with each other, which requires many more steps.

2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- Pseudocode 1 is easier to understand because its logic is simpler and more direct. It starts with the first number as the maximum and checks each following number to see if it is larger. Its variable name “max” is also meaningful and clearly shows what the algorithm is looking for.


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- Pseudocode #1 would be easier to update with min and max in mind since it is simpler and has fewer lines.


4. Testability
Which algorithm is easier to test with different inputs? Why?
- Pseudocode #2 will test well with more inputs since it has longer lines and is much more detailed; this will make including various amount of outputs easier and will make the algorithm run much more smoothly.

5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- The code should verify whether the list is void, while also verifying if the variables in the list are numbers or letters. Both codes don't do any of these however so they both need to be updated for they don't have a command that does this.

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
- Pseudocode #1 is the best one to use between the 2 since It works faster and is a more simpler code to use than the second pseudocode. Due to it being a smaller code, it's easier to update and change something when you encounter an error.
