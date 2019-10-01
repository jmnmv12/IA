# Map

Map applies a function to all the items in an input_list. Here is the blueprint:

```
map(function_to_apply, list_of_inputs)
```
Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:

```
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

```

Map allows us to implement this in a much simpler and nicer way. Here you go:
```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

# Reduce

Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

So the normal way you might go about doing this task in python is using a basic for loop:
```
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

#product = 24
```
Now let’s try it with reduce:
```
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

#Output: 24
```


Based on https://book.pythontips.com/en/latest/map_filter.html


