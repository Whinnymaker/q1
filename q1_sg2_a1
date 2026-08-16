# q1_sg2_a1
Annex B
# Computational Thinking Exercise: "Smart Vending Machine"
Section: 9-PINATUBO 
Score:____________

C# / Name: 4,5,6 / ESDRELON, DUCUSIN, DE LEON
Date: 8/16/2026


Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The vending machine does not reliably process students' purchases, resulting in incorrect change, unavailable items, wrong items being dispensed, and slow service when many students use it at the same time.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Potential scarcity of items - The machine may run out of certain snacks or drinks without notifying anyone.
2. Prone to wrong button pressing - Students may accidentally press the wrong button and receive an incorrect item.
3. Slow maintenance - Items may not be restocked quickly when they run out.
4. Prone to giving wrong change - The machine may incorrectly calculate or dispense the customer's change.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

| Sub-Problem                    | CT Skill                                         | Example Solution                                                                                                                                                                                     |
| ------------------------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Potential scarcity of items    | **Pattern Recognition and Abstraction**          | Monitor the quantity of each item and identify when an item reaches a low-stock level. The machine can display a notification such as **"Low Stock"** or **"Out of Stock."**                         |
| Prone to wrong button pressing | **Algorithmic Thinking**                         | Create a clear sequence that checks the selected button and displays the corresponding item before confirming the purchase. The student can confirm their selection before the machine dispenses it. |
| Slow maintenance/restocking    | **Decomposition and Algorithmic Thinking**       | Divide the maintenance process into smaller steps: check inventory, identify empty slots, notify the assigned staff, and restock the necessary items.                                                |
| Prone to giving wrong change   | **Algorithmic Thinking and Pattern Recognition** | Create a precise calculation process that compares the amount inserted with the item's price and calculates the correct change before dispensing it.                                                 |



Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)

Check if Vending Machine is ready

IF machine is busy:
  display "please wait"
  wait until the current transaction is finished
ELSE:
  accept student's payment
  display available items
  student selects an item

  IF selected item is available
    check payment
    calculate change
    dispense item
    dispense correct change
    update item inventory
  ELSE
    display "item unavailable"
    return payment
