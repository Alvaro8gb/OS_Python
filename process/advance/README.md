The sum of consecutive integers from 1 to $n $ can be calculated using the arithmetic sum formula:

$$ \text{Sum} = \frac{n \cdot (n + 1)}{2} $$

In this case, if you want to calculate the sum of numbers from 1 to 1001, you substitute $n = 1001 $ into the formula:

$$ \text{Sum} = \frac{1001 \cdot (1001 + 1)}{2}  = 500500$$

You can use this formula to calculate the sum without explicitly adding all the numbers. In Python, you can implement it like this:

```python
n = 1001
sum_result = (n * (n + 1)) // 2
print("Sum of numbers from 1 to 1001:", sum_result)
```

This will output the sum of numbers from 1 to 1001 using the arithmetic sum formula.