# Stacks

## Introduction
Have you ever made pancakes for a large number of people, and by the time you are finally able to eat all that is left are the cold and crushed pancakes from the bottom of the stack? This is because pancakes, just like lists in a stack data structure, work on a Last-In First-Out structure, or "LIFO", where the last item pushed, meaning added, is the first item popped, or removed.

    "So the last shall be first, and the first last: for many be pushed, but few popped."
    -Unknown

## Real World Examples
There are as many real world examples of stacks as there are objects that can be piled one on top of another, and more than a few others.

We have:
* Pancakes
* Firewood
* People crammed into a van
* Food in a fridge, even though we know we shouldn't

Anything where the last thing added to the structure is the first thing that will be removed. 

![Stack of Rocks](Final/Picture/stone-tower-4519290_640.jpg)

## Software Example
One of the most common uses of a stack is the Undo function. Most programs, especially when editting is involved, will store each command on a stack. Take the photo of the rocks seen above. Below is a list of the actions I took to add the arrows, in reverse order to demonstrate the top-down order of a stack.
* Change text to bold
* Add "Not This" text
* Create rightward pointing arrow
* Change text to bold
* Add "Take This" text
* Create leftward pointing arrow

If I were to hit CTRL + Z it would pop, or remove, the command from the top of the stack, making the **"Not This"** text no longer bold. (When popped, these commands are actually pushed to a Redo stack, triggered by CTRL + Y) After the Undo function is executed the stack is as follows:
* Add "Not This" text
* Create rightward pointing arrow
* Change text to bold
* Add "Take This" text
* Create leftward pointing arrow

Undoing again would now remove the "Not This" text, as it is now at the top of the stack.

## Operations
Operation | Code | Description
--------- | ---- | -----------
def push(item) | stack.append(item) | Adds an item to the top of the stack
def pop() | stack.pop() | Removes the item from the top of the stack (can be stored in a variable)
def size() | size = len(stack) | Show how many items are in the stack
def peek() | stack[-1] | This allows us to see what is on top of the stack without removing it
def empty() | if len(stack) == 0 | Tells us if there are no items in a stack

## Big O Notation
One of the best parts about stacks is that every operation listed above has a performance of O(1). No searching or rearranging is required.

## Problems to Solve
Am I smart enough to know the longest word in the English language that is in alphabetical order? A-L-M-O-S-T:
[Problem](Python\stack_1.py)

[Solution](Python\stack_1_solution.py)

Delete the middle of a stack:

[Problem](Python\stack_2.py)

[Solution](Python\stack_2_solution.py)
