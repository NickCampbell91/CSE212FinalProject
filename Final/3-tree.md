# Trees

## Introduction
Remember when in Alice in Wonderland where the Mad Hatter and the Hare asked Alice for her story but Alice didn't know where to start?

    "Start from the beginning!" exclaimed the Hare.

    "And when you get to the end," added the Mad Hatter, "stop."

This, as you may assume from who said it, is utter madness. Computers are not smart, but they are obedient, so they will start from the beginning. Alice knew where her story started, but you know who didn't? Chunk from The Goonies. To make my point I will include the whole quote, but **feel free to skip ahead**.

![Interrogation](Picture\goonies1.jpg)

    "Tell us everything,"

    "Everything? Okay. I'll talk. In third grade, I cheated on my history exam. In fourth grade, I stole my uncle Max’s toupee and I glued it on my face when I was Moses in my Hebrew School play. In fifth grade, I knocked my sister Edie down the stairs and I blamed it on the dog… when my mom sent me to the summer camp for fat kids and then they served lunch I got nuts and I pigged out and they kicked me out… but the worst thing I ever done – I mixed a pot of fake puke at home and then I went to this movie theater, hid the puke in my jacket, climbed up to the balcony and then, t-t-then, I made a noise like this: hua-hua-hua-huaaaaaaa – and then I dumped it over the side, all over the people in the audience. And then, this was horrible, all the people started getting sick and throwing up all over each other. I never felt so bad in my entire life."

Here Chunk is your list and Francis is your program searching through it. It starts from the beginning and stops when the right information is found. This has a big O notation of O(n), which isn't bad, but isn't good either. 

With a little extra effort we can create a data structure where with each step the remaining information to search through is reduced by half. We call this data structure a binary tree because the data is split into a series of branches.

## Vocabulary
![Tree labels](Picture\1_PWJiwTxRdQy8A_Y0hAv5Eg.png)

Name | Description
---- | -----------
Root | The staring point of the tree. On your family tree this would be you.
Leaf Nodes | The circles seen in the tree above. Denotes the position, not the value.
Key | The value in the node.
Parent | A node with branches beneath it.
Children | The branches beneath the parent node.
Siblings | Nodes than have the same parent
Subtree | A subsection of the tree.
Height | The number of level. The tree above would have a height of 5.


## Real World Example
Imagine you are in class when your professor tells you, "Turn to page 394." What do you do? Do you start from the beginning and move forward one page at a time? Of course not. The class would be over by the time you got to your page. 

You would open the book more or less where you think the page is, see if you current page is greater than or less than 394. If it is less than 394 you would repeat the process somewhere further in the book. What your are doing is a recursive function called BST (Binary Search Tree).

## Recursion
Recursive functions are any function that calls on itself. Like the example just given with the book, the function was to open to a new page, and the recursive aspect was when the function was called again with new information as to which page would be attempted. It is important that the function has an if statement offering a condition in which the recursive function will end, otherwise the function will try to go on forever. Some languages, like Python, set a hard limit of the number of recursions, but it is still a broken function. 

See below for an example of a recursive function in code.

## Software Example
![Basic Tree](Picture\basic_tree.png)

The picture above depicts a very simple binary tree with small integers. To demonstrate how your computer would search though a tree such as this, lets look for a number.

```
    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)
        else:
            return True
```

The first function is automatically called if the user uses the "in" function to see if a value is in a tree.
```
print(8 in tree) 
```
This call should print "True", as proven by a glance at the tree.

It also tells the computer to begin the search at the root of the tree, i.e. 5. The "data" passed in is the 8, and the "node" passed to the next function is the root. The _contains function will first ask if the data is less than or greater than the value in the current node. 8 is greater than 5, so the second if statement is triggered. It then asks if there are any nodes greater than the 5. There are, so the computer calls the function again, only now starting at the node to the right of the root, which holds 7.

Second verse, same as the first. Is 8 less than 7? No. Is 8 greater than 7? Yes. Is there a node to the right of 7? Yes. The function is called again, only now starting at the node to the right of 7.

Is 8 less than 8? No. Is 8 greater than 8? No. Logically this can only mean one thing, triggering the else statement to return True. The tree does contain 8.


## Operations
Operation | Description
--------- | -----------
Insert(value) | Adds a value into the tree.
remove(value) | Removes a value from a tree. If the node had one or more children, one of them must replace the node as the new parent.
contains(value) | Asks if the value can be found in the tree, as demonstrated above.
height(node) | Returns the height originating at the given node.
size() | Returns the number of nodes found in the tree. 
empty() | Returns true if the root is empty.

## Big O Notation
Size() and empty() are each O(1), as the size value is stored in the BST class and the root is found immediately. The others are O(log n) as the amount of unsearched data remaining is reduced with every step of the process.

## Problems to Solve

Insert:

[Problem](Python\tree_1.py)

[Solution](Python\tree_1_solution.py)

Remove:

[Problem](Python\tree_2.py)

[Solution](Python\tree_2_solution.py)