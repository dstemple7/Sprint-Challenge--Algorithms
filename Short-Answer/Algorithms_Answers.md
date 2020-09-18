#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) this is a while loop and the runtime complexity is O(n)

b) this is a while loop nested in a foor loop and the runtime complexity is O(n^2)

c) this is a recursive if statement and the runtime complexity is O(n)

## Exercise II

A) since the number in question is a floor and assuming the floors are in order from 1-n, we could use a binary search which would go as follows:
1) find the length of n, in this example we're gonna say 100
2) find the midpoint of n dividing the lenght in half, so 50 in this case
3) test this point by dropping an egg
4) asses: if the egg breaks, we're too high; if the egg doesn't break, we may be too low.
    a) if the egg broke, we move halfway between the midpoint and the start point, 25 in this case
    b) if the egg didn't break, we move halfway between the midpoint and the end point, 75 in this case.
5) whichever new point we're at, we drop an egg and repeat/recurse the process until we're at f, the highest floor in which we can drop an egg without it breaking

The runtime complexity for binary search is O(1) in the best case, O(n) in the worst case, and O(log n) on average:
-In the best case, the length is 1 or on the first iteration the goal is found, binary search is O(1)
-In the worst case, the length is n and binary search has to touch each element once, then it is O(n)
-On average, binary search runs on logarithmic time, which stated simply means it takes a fraction of n, and is O(log n)
