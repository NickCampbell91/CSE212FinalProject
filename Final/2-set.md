# Sets

## Introduction
Sets are like lists in python, but different in several key ways. The elements are both unordered and unindexed, meaning that you can print it multiple times and see it printed in multiple orders. The items are unchangeable, so if an element needs to be changed it must be removed and replaced. And lastly sets do not allow for duplicates.

## Real World Example
Imagine children being loaded onto a school bus. The order can change with every trip, the driver obviously can't change the children, and, for obvious reasons, there can be no duplicates. 

## Software Example
If you were to store usernames on your website, they would by definition have to be unique, unchangable, and the arrangement would not matter. 

Let's imagine you are trying to sign up to play an MMO. Currently there are only four other players, for the sake of the example.

```
users = set([n00bSlayer420, EdgeLord666, xXPANCAKESXx, KiritoSama])
```

You want to be taken seriously in the servers, so you come up with the perfect username. You fill out the website's text boxes, but the backend look a little like this:

```
users.add(EdgeLord666)
```

Sadly, this username was already taken. 

Somewhere out there the true EdgeLord666 is taking issue with there only being three other players in a Massively Mulpiplayer Online game, as proven by the code below.

```
print(len(users))
4
```

So he quits the game, which behind the scenes looks like:

```
users.remove(EdgeLord666)
```

## Operations
Operation | Code | Description
--------- | ---- | -----------
def add(item) | my_set.add(item) | Adds an item somewhere into the set.
def remove() | my_set.remove(item) | Removes the item from the set. Will throw error if item is not there.
def discard() | my_set.discard(item) | Removes the item from the set. Will not throw error if item is not there.
def member(item) | if item in my_set | Returns boolean showing if item is in set
def size() | length = len(my_set) | Returns length of the stack

## Big O Notation
One of the best parts about sets is that every operation listed above has a performance of O(1), assuming good conflict resolution. No searching or rearranging is required.

## Problems to Solve

Intersection:

[Problem](Python\set_1.py)

[Solution](Python\set_1_solution.py)

Union:

[Problem](Python\set_2.py)

[Solution](Python\set_2_solution.py)