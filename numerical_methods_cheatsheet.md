# Numerical Methods - MATLAB Cheat Sheet

---

## 1. ROOT FINDING

### Bisection Method
Repeatedly halves the interval until root is found. Needs `f(a)*f(b) < 0`.

```matlab
f = @(x) x^3 - x - 2;  % change your function here
a = 1; b = 2;           % initial interval
tol = 1e-6;

while (b-a)/2 > tol
    c = (a+b)/2;
    if f(c) == 0, break; end
    if f(a)*f(c) < 0
        b = c;
    else
        a = c;
    end
end
fprintf('Root = %.6f\n', c);
```

---

### False Position (Regula Falsi)
Like bisection but uses a line through f(a) and f(b) to estimate root — converges faster.

```matlab
f = @(x) x^3 - x - 2;
a = 1; b = 2;
tol = 1e-6;

for i = 1:100
    c = b - f(b)*(b-a)/(f(b)-f(a));  % key formula
    if abs(f(c)) < tol, break; end
    if f(a)*f(c) < 0
        b = c;
    else
        a = c;
    end
end
fprintf('Root = %.6f\n', c);
```

---

## 2. LINEAR EQUATIONS

### Gauss-Jacobi
Uses **old values** for all updates in each iteration.

```matlab
A = [4 1 -1; 2 7 1; 1 -3 12];   % coefficient matrix
b = [3; 19; 31];                  % RHS
n = length(b);
x = zeros(n,1);   % initial guess

for iter = 1:100
    x_new = zeros(n,1);
    for i = 1:n
        s = b(i);
        for j = 1:n
            if j ~= i, s = s - A(i,j)*x(j); end
        end
        x_new(i) = s / A(i,i);
    end
    if norm(x_new - x) < 1e-6, break; end
    x = x_new;
end
disp(x);
```

---

### Gauss-Seidel
Uses **new values immediately** — converges faster than Jacobi.

```matlab
A = [4 1 -1; 2 7 1; 1 -3 12];
b = [3; 19; 31];
n = length(b);
x = zeros(n,1);

for iter = 1:100
    x_old = x;
    for i = 1:n
        s = b(i);
        for j = 1:n
            if j ~= i, s = s - A(i,j)*x(j); end  % uses updated x
        end
        x(i) = s / A(i,i);
    end
    if norm(x - x_old) < 1e-6, break; end
end
disp(x);
```

---

## 3. INTERPOLATION

### Newton's Forward Difference
Use when point is near the **beginning** of the table.

```matlab
x = [0 1 2 3 4];
y = [1 1.5 3 5.5 9];
n = length(x);
h = x(2)-x(1);

% Build difference table
D = zeros(n,n);
D(:,1) = y';
for j = 2:n
    for i = 1:n-j+1
        D(i,j) = D(i+1,j-1) - D(i,j-1);
    end
end

xp = 1.5; % point to interpolate
s = (xp - x(1)) / h;
result = D(1,1);
term = 1;
for k = 1:n-1
    term = term * (s-k+1) / k;
    result = result + term * D(1,k+1);
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

---

### Newton's Backward Difference
Use when point is near the **end** of the table.

```matlab
x = [0 1 2 3 4];
y = [1 1.5 3 5.5 9];
n = length(x);
h = x(2)-x(1);

D = zeros(n,n);
D(:,1) = y';
for j = 2:n
    for i = n:-1:j
        D(i,j) = D(i,j-1) - D(i-1,j-1);
    end
end

xp = 3.5;  % point near end
s = (xp - x(n)) / h;
result = D(n,1);
term = 1;
for k = 1:n-1
    term = term * (s+k-1) / k;
    result = result + term * D(n,k+1);
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

---

### Lagrange Interpolation
Works for **unequal spacing**. No difference table needed.

```matlab
x = [0 1 2 4];
y = [1 1.5 3 9];
xp = 3;  % point to interpolate

n = length(x);
result = 0;
for i = 1:n
    L = 1;
    for j = 1:n
        if j ~= i
            L = L * (xp - x(j)) / (x(i) - x(j));
        end
    end
    result = result + L * y(i);
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

---

## 4. NUMERICAL INTEGRATION

### Simpson's 1/3 Rule
Needs **even number** of intervals (n even). Weights: 1, 4, 2, 4, ..., 1

```matlab
f = @(x) 1./(1+x);   % function to integrate
a = 0; b = 1;
n = 4;  % must be even
h = (b-a)/n;
x = a:h:b;
y = f(x);

result = y(1) + y(end);
for i = 2:n
    if mod(i,2) == 0
        result = result + 4*y(i);
    else
        result = result + 2*y(i);
    end
end
result = result * h/3;
fprintf('Integral = %.6f\n', result);
```

---

### Simpson's 3/8 Rule
Needs **n divisible by 3**. Weights: 1, 3, 3, 2, 3, 3, ..., 1

```matlab
f = @(x) 1./(1+x);
a = 0; b = 1;
n = 6;   % must be multiple of 3
h = (b-a)/n;
x = a:h:b;
y = f(x);

result = y(1) + y(end);
for i = 2:n
    if mod(i-1, 3) == 0
        result = result + 2*y(i);
    else
        result = result + 3*y(i);
    end
end
result = result * 3*h/8;
fprintf('Integral = %.6f\n', result);
```

---

## 5. ODE / NUMERICAL DIFFERENTIATION

### Euler's Method
Simplest ODE solver. `y_next = y + h*f(x,y)`. Low accuracy.

```matlab
f = @(x,y) x + y;     % dy/dx = f(x,y)
x0 = 0; y0 = 1;       % initial condition
xf = 0.5; h = 0.1;    % end point & step size

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    y = y + h * f(x, y);
    x = x + h;
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

---

### Heun's Method (Improved Euler)
Predicts with Euler, then **corrects** using average slope.

```matlab
f = @(x,y) x + y;
x0 = 0; y0 = 1;
xf = 0.5; h = 0.1;

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    k1 = f(x, y);
    k2 = f(x+h, y+h*k1);   % predictor
    y = y + h*(k1+k2)/2;    % corrector (average)
    x = x + h;
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

---

### Runge-Kutta 4th Order (RK4)
Most accurate of the three. Uses **4 slope estimates**.

```matlab
f = @(x,y) x + y;
x0 = 0; y0 = 1;
xf = 0.5; h = 0.1;

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    k1 = f(x, y);
    k2 = f(x+h/2, y+h*k1/2);
    k3 = f(x+h/2, y+h*k2/2);
    k4 = f(x+h,   y+h*k3);
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4);
    x = x + h;
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

---

## ⚡ Quick Cheat Notes

| Method | Key Formula to Remember |
|--------|------------------------|
| Bisection | `c = (a+b)/2` |
| False Position | `c = b - f(b)*(b-a)/(f(b)-f(a))` |
| Jacobi | Uses old `x` for all updates |
| Seidel | Uses new `x` immediately |
| Simpson 1/3 | `h/3 * (1,4,2,4,...,1)` |
| Simpson 3/8 | `3h/8 * (1,3,3,2,3,3,...,1)` |
| Euler | `y = y + h*f(x,y)` |
| Heun's | `y = y + h*(k1+k2)/2` |
| RK4 | `y = y + h/6*(k1+2k2+2k3+k4)` |

---

*Good luck on your final! 🎯*
