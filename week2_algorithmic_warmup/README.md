####Runtime
Runtime of a program vary with multiple factors such as the computers's speed, 
architecture, memory profile and so on. Hence we use Asymptotic Runtime, that 
scales with the input size n.

Example : log n < n^(1/2)< n < n log n < n^2 < 2^n 

####Bio-O Notation
f(n) = O(g(n)) or f <= g if there exists constants N and c so that for all
n >= N, f(n) < c * g(n)

- Multiplicative constant can be removed [7n^3 = O(n^3);]
- n^a < n^b for 0 < a < b [n = O(n^2); n^(1/2) = O(n);]
- n^a < n^b for a > 0; b > 1 [n^5 = O((2^(1/2)))^n; n^100 = O(1.1^n);] 
- (log n)^a < n^b [(log n)^3 = O(n^(1/2)); n log n = O(n^2)]
- Smaller terms can be eliminated [n^2 + n = O(n^2)]  

It basically means f(n) grows no faster then O(g(n))
Eg: 5n^2 = O(n^2); 5n^2 = O(n^3); both are correct, it means 5n^2 grows no 
faster than the rest.


 
  
