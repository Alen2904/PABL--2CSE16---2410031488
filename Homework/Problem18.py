from typing import List

def factorial_digits(n: int) -> List[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return [int(d) for d in str(fact)]

if __name__ == "__main__":
    print(factorial_digits(5))  
    print(factorial_digits(10))  
    print(factorial_digits(1))   
