# stepbysierp
A breadth-first Sierpinski triangle, using generators. It has been optimised a lot so that each stack frame needs only track coordinates, and crucially they share triangle dimension information. Originally, whenever a new depth was reached, the program stuttered as it had to create an exponential number of new generators with new calculations. It looks like this:

![screenshot](https://github.com/goedel-gang/stepbysierp/blob/master/screenshot.png)
