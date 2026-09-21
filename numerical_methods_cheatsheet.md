# Numerical Methods - MATLAB Cheat Sheet

---

## 1. ROOT FINDING

> **Core Idea:** Root finding answers the question — *"at what value of x does f(x) = 0?"*
> Both methods below need you to start with two points `a` and `b` where the function is on **opposite sides of zero** (one positive, one negative). This guarantees a root exists between them.

---

### Bisection Method

**What it does:**
Imagine you're guessing a number between 1–100. The simplest strategy is to always guess the middle. That's bisection. You check the midpoint `c = (a+b)/2`, then decide which half still contains the root, and throw the other half away. Repeat until the interval is tiny enough.

**Why it works:**
If `f(a)` and `f(b)` have opposite signs, the curve must cross zero somewhere between them (Intermediate Value Theorem). After each step, the search space is cut in half.

**Line-by-line breakdown:**
```matlab
f = @(x) x^3 - x - 2;  % Define your equation (set it = 0 form)
a = 1; b = 2;           % Your starting bracket — f(1)<0, f(2)>0
tol = 1e-6;             % Stop when interval is smaller than this

while (b-a)/2 > tol     % Keep going until interval is tiny
    c = (a+b)/2;        % CORE STEP: pick the midpoint
    if f(c) == 0, break; end          % Lucky exact hit
    if f(a)*f(c) < 0    % Root is in LEFT half (a to c)
        b = c;          %   → shrink right boundary
    else                % Root is in RIGHT half (c to b)
        a = c;          %   → shrink left boundary
    end
end
fprintf('Root = %.6f\n', c);
```

**Key rule:** `f(a)*f(c) < 0` means they have opposite signs → root is between a and c.

---

### False Position (Regula Falsi)

**What it does:**
Same idea as bisection (keep a bracket, shrink it), but instead of always picking the exact midpoint, it draws a **straight line** between `(a, f(a))` and `(b, f(b))` and picks where that line crosses zero. This is smarter than always picking the middle — it leans toward where the root probably is.

**Why it's faster:**
If the function is steeper on one side, the straight line will predict a better guess than the simple midpoint.

**Line-by-line breakdown:**
```matlab
f = @(x) x^3 - x - 2;
a = 1; b = 2;
tol = 1e-6;

for i = 1:100
    c = b - f(b)*(b-a)/(f(b)-f(a));  % Where the line through (a,f(a))
                                       % and (b,f(b)) hits zero
    if abs(f(c)) < tol, break; end    % Stop if f(c) is close enough to 0
    if f(a)*f(c) < 0                  % Root is between a and c
        b = c;
    else                               % Root is between c and b
        a = c;
    end
end
fprintf('Root = %.6f\n', c);
```

**Bisection vs False Position:**
| | Bisection | False Position |
|---|---|---|
| How c is picked | Always midpoint | Linear interpolation |
| Convergence | Slower | Faster |
| Reliability | Very safe | Also safe |

---

## 2. LINEAR EQUATIONS (Iterative Solvers)

> **Core Idea:** You have a system like `Ax = b` (multiple equations, multiple unknowns). Instead of solving exactly (like Gaussian elimination), these methods *guess and improve* — they start with x = 0 and keep updating until the answer stops changing.
>
> **Requirement:** The matrix should be *diagonally dominant* — each diagonal element must be larger than the sum of other elements in its row. This ensures convergence.

---

### Gauss-Jacobi

**What it does:**
Each iteration, compute ALL new values of x using ONLY the old values. It's like everyone updating simultaneously without seeing each other's new answers yet.

**Think of it like:** A group of students solving a system, but they all write their answers at the same time on separate papers without seeing others' new answers.

**Line-by-line breakdown:**
```matlab
A = [4 1 -1; 2 7 1; 1 -3 12];  % The coefficient matrix (left side of equations)
b = [3; 19; 31];                 % The right-hand side values
n = length(b);                   % Number of unknowns
x = zeros(n,1);                  % Start with x = [0, 0, 0] as initial guess

for iter = 1:100                 % Do at most 100 iterations
    x_new = zeros(n,1);          % Fresh storage for new values
    for i = 1:n                  % For each equation i
        s = b(i);                % Start with the RHS value
        for j = 1:n
            if j ~= i            % Subtract all terms EXCEPT the diagonal
                s = s - A(i,j)*x(j);  % Using OLD x values
            end
        end
        x_new(i) = s / A(i,i);  % Solve for x(i): divide by diagonal
    end
    if norm(x_new - x) < 1e-6, break; end  % Stop if change is tiny
    x = x_new;                   % REPLACE all at once (key Jacobi feature)
end
disp(x);
```

**The formula being applied each time:**
`x_i = (b_i - sum of A_ij * x_j for j≠i) / A_ii`

---

### Gauss-Seidel

**What it does:**
Same as Jacobi, but as soon as you compute a new `x(i)`, you immediately use it for the next equations in the same iteration. You don't wait for the full round to finish.

**Think of it like:** Same group of students, but they pass their answer immediately to the next person — so later students in each round have fresher information.

**Why it's faster:** Using the most up-to-date values makes each guess better, so you need fewer iterations.

**Line-by-line breakdown:**
```matlab
A = [4 1 -1; 2 7 1; 1 -3 12];
b = [3; 19; 31];
n = length(b);
x = zeros(n,1);

for iter = 1:100
    x_old = x;              % Save a copy to check convergence later
    for i = 1:n
        s = b(i);
        for j = 1:n
            if j ~= i
                s = s - A(i,j)*x(j);  % Uses UPDATED x if j < i (already computed)
            end                        % Uses OLD x if j > i (not yet computed)
        end
        x(i) = s / A(i,i); % Update x(i) IMMEDIATELY — next equations will use this
    end
    if norm(x - x_old) < 1e-6, break; end  % Stop when barely changing
end
disp(x);
```

**The only difference from Jacobi:** No `x_new` array — we write directly into `x`, so new values are used right away.

---

## 3. INTERPOLATION

> **Core Idea:** You have a table of known (x, y) points. Someone asks "what is y at x = 2.7?" (a point not in your table). Interpolation estimates that value by fitting a curve through the known points.
>
> Think of it as: filling in the blanks between data points.

---

### Newton's Forward Difference

**When to use:** When the x-point you want is near the **start** of the table.

**What it does:** Builds a "difference table" (a triangle of differences between y values), then uses a polynomial formula to estimate the unknown point. The formula adds correction terms, each based on how far you are from the first point.

**Line-by-line breakdown:**
```matlab
x = [0 1 2 3 4];    % Known x values (equally spaced!)
y = [1 1.5 3 5.5 9]; % Known y values
n = length(x);
h = x(2)-x(1);       % Step size (spacing between x values)

% --- Build the Forward Difference Table ---
D = zeros(n,n);      % D is the difference table
D(:,1) = y';         % First column = original y values
for j = 2:n
    for i = 1:n-j+1
        D(i,j) = D(i+1,j-1) - D(i,j-1);  % Each cell = cell below minus cell left
    end
end
% D(1,1)=y0, D(1,2)=Δy0, D(1,3)=Δ²y0, etc. (first row of differences)

xp = 1.5;            % The x value you want to find y for
s = (xp - x(1)) / h; % Normalized distance from start of table

result = D(1,1);     % Start with y0
term = 1;
for k = 1:n-1
    term = term * (s-k+1) / k;        % Newton's forward formula terms
    result = result + term * D(1,k+1); % Add each correction
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

**The difference table for this example looks like:**
```
y0=1   Δy=0.5   Δ²y=1   Δ³y=0   ...
y1=1.5 Δy=1.5   Δ²y=1   ...
y2=3   Δy=2.5   ...
y3=5.5 ...
y4=9
```

---

### Newton's Backward Difference

**When to use:** When the x-point you want is near the **end** of the table.

**What it does:** Same idea as forward, but builds the difference table from the bottom up and uses the last row. The formula measures distance from the **last** point.

**Line-by-line breakdown:**
```matlab
x = [0 1 2 3 4];
y = [1 1.5 3 5.5 9];
n = length(x);
h = x(2)-x(1);

% --- Build the Backward Difference Table ---
D = zeros(n,n);
D(:,1) = y';
for j = 2:n
    for i = n:-1:j              % Fill from bottom to top (opposite of forward)
        D(i,j) = D(i,j-1) - D(i-1,j-1);  % cell = cell above minus cell left
    end
end
% D(n,1)=yn, D(n,2)=∇yn, D(n,3)=∇²yn (last row of differences)

xp = 3.5;            % Point near the END of the table
s = (xp - x(n)) / h; % Normalized distance from END of table (will be negative or small)

result = D(n,1);     % Start with last y value
term = 1;
for k = 1:n-1
    term = term * (s+k-1) / k;        % Backward formula terms (note s+k-1, not s-k+1)
    result = result + term * D(n,k+1); % Add each correction using last row
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

**Forward vs Backward — when to pick which:**
| | Forward | Backward |
|---|---|---|
| Use when xp is near... | Start of table | End of table |
| s is measured from... | First point x(1) | Last point x(n) |
| Uses row... | First row of D | Last row of D |

---

### Lagrange Interpolation

**When to use:** When x values are **NOT equally spaced** (or any time, really — it always works).

**What it does:** For each known point, it creates a "basis polynomial" L_i(x) that equals 1 at x_i and 0 at all other known points. Then the answer is just a weighted sum: `result = Σ y_i * L_i(xp)`.

**Why it's elegant:** No difference table needed. Works with any spacing.

**Line-by-line breakdown:**
```matlab
x = [0 1 2 4];   % x values (can be unequal spacing!)
y = [1 1.5 3 9]; % y values
xp = 3;          % Point to estimate

n = length(x);
result = 0;
for i = 1:n              % For each known point i
    L = 1;               % Start building the basis polynomial L_i
    for j = 1:n
        if j ~= i
            L = L * (xp - x(j)) / (x(i) - x(j));
            % Numerator: (xp - every other x)
            % Denominator: (x_i - every other x)
            % This makes L=1 when xp=x(i), and L=0 at all other x(j)
        end
    end
    result = result + L * y(i);  % Add contribution: y_i weighted by L_i
end
fprintf('f(%.2f) = %.6f\n', xp, result);
```

**Intuition example with 2 points:**
If you have (0,1) and (2,3), the Lagrange formula just gives you the straight line between them. With more points, it fits a higher-degree curve.

---

## 4. NUMERICAL INTEGRATION

> **Core Idea:** You want to find the area under a curve f(x) from x=a to x=b, but you either can't integrate it analytically, or you only have table values. Simpson's methods approximate the area by fitting simple curves (parabolas) over small strips.

---

### Simpson's 1/3 Rule

**What it does:** Divides the interval into `n` equal strips (n must be even). Fits a parabola over every **pair** of strips. The weights follow the pattern **1, 4, 2, 4, 2, ..., 4, 1**.

**Why those weights (1,4,2,...)?**
- The first and last points get weight **1**
- Interior points at even positions (2nd, 4th, ...) get weight **4** (these are the midpoints of each parabola)
- Interior points at odd positions (3rd, 5th, ...) get weight **2** (these are shared between two parabolas)

**Line-by-line breakdown:**
```matlab
f = @(x) 1./(1+x);  % Function to integrate
a = 0; b = 1;        % Integration limits
n = 4;               % Number of strips — MUST be even
h = (b-a)/n;         % Width of each strip
x = a:h:b;           % x points: [0, 0.25, 0.5, 0.75, 1]
y = f(x);            % y values at those points

result = y(1) + y(end);   % First and last get weight 1
for i = 2:n               % Loop over interior points
    if mod(i,2) == 0      % Even index → weight 4
        result = result + 4*y(i);
    else                   % Odd index → weight 2
        result = result + 2*y(i);
    end
end
result = result * h/3;    % Multiply by h/3 (the Simpson 1/3 formula factor)
fprintf('Integral = %.6f\n', result);
```

**Pattern visualization:**
```
Points:  x0   x1   x2   x3   x4
Weights:  1    4    2    4    1
```

---

### Simpson's 3/8 Rule

**What it does:** Similar to 1/3, but fits a **cubic** (degree-3 curve) over every **3 strips**. So n must be divisible by 3. Weights follow **1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1**.

**Why those weights (1,3,3,2,...)?**
- First and last: weight **1**
- Points at positions that are multiples of 3 from the start (interior): weight **2** (shared between two cubics)
- All other interior points: weight **3**

**Line-by-line breakdown:**
```matlab
f = @(x) 1./(1+x);
a = 0; b = 1;
n = 6;              % MUST be divisible by 3
h = (b-a)/n;
x = a:h:b;
y = f(x);

result = y(1) + y(end);    % First and last → weight 1
for i = 2:n                % Loop interior points
    if mod(i-1, 3) == 0    % Every 3rd interior point → weight 2
        result = result + 2*y(i);
    else                    % All others → weight 3
        result = result + 3*y(i);
    end
end
result = result * 3*h/8;   % Multiply by 3h/8 (the 3/8 formula factor)
fprintf('Integral = %.6f\n', result);
```

**Pattern visualization:**
```
Points:  x0   x1   x2   x3   x4   x5   x6
Weights:  1    3    3    2    3    3    1
```

**1/3 vs 3/8:**
| | Simpson 1/3 | Simpson 3/8 |
|---|---|---|
| Strips per piece | 2 | 3 |
| Curve fitted | Parabola | Cubic |
| n requirement | Even | Multiple of 3 |
| Factor | h/3 | 3h/8 |
| Accuracy | Good | Slightly better |

---

## 5. ODE SOLVERS (Numerical Differentiation)

> **Core Idea:** You have a differential equation like `dy/dx = f(x, y)` with a starting point `(x0, y0)`. You can't (or don't want to) solve it analytically. Instead, you take small steps of size `h` and estimate where y goes next.
>
> Think of it like driving in fog — you can only see a little ahead, so you take small steps, check your direction, and move forward.

---

### Euler's Method

**What it does:** The simplest possible approach. At each point, look at the slope `f(x,y)` and just walk straight in that direction by step h. It's like following a compass that only updates at each step.

**Formula:** `y_next = y + h * f(x, y)`

**Why it's inaccurate:** The slope changes between steps, but you're assuming it stays constant. Bigger h = bigger error.

**Line-by-line breakdown:**
```matlab
f = @(x,y) x + y;   % The ODE: dy/dx = x + y
x0 = 0; y0 = 1;     % Starting point (initial condition)
xf = 0.5; h = 0.1;  % Go from x=0 to x=0.5 in steps of 0.1

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    y = y + h * f(x, y);   % CORE: move y using current slope
    x = x + h;              % Move x forward by one step
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

**Visualization:**
```
Exact curve:  ~~~~/
Euler steps:  ___/  (staircase approximation)
```
Smaller h → steps are tinier → staircase looks more like the curve.

---

### Heun's Method (Improved Euler / Predictor-Corrector)

**What it does:** Fixes Euler's weakness by using **two slope estimates** per step:
1. **Predict** where you'd end up using Euler (slope at start)
2. **Correct** by averaging the slope at the start AND the predicted end point

**Formula:**
- k1 = slope at current point
- k2 = slope at predicted next point
- `y_next = y + h*(k1+k2)/2`

**Line-by-line breakdown:**
```matlab
f = @(x,y) x + y;
x0 = 0; y0 = 1;
xf = 0.5; h = 0.1;

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    k1 = f(x, y);              % Slope at current point
    k2 = f(x+h, y+h*k1);      % Slope at the Euler-predicted next point
    y = y + h*(k1+k2)/2;       % Use AVERAGE of both slopes → more accurate
    x = x + h;
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

**Analogy:** Euler is like driving while only looking at the road right in front. Heun's looks ahead too, then splits the difference — much smoother.

---

### Runge-Kutta 4th Order (RK4)

**What it does:** The gold standard for ODE solving. Uses **4 slope estimates** per step, weighted cleverly to cancel out error terms. Much more accurate than Euler or Heun's with the same step size.

**The 4 slopes:**
- **k1** = slope at the start of the interval
- **k2** = slope at the midpoint, using k1 to get there
- **k3** = slope at the midpoint again, using k2 to get there (refinement)
- **k4** = slope at the end, using k3 to get there

**Final update:** `y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)`
Note the weights: **1, 2, 2, 1** (midpoint slopes count double)

**Line-by-line breakdown:**
```matlab
f = @(x,y) x + y;
x0 = 0; y0 = 1;
xf = 0.5; h = 0.1;

x = x0; y = y0;
fprintf('x=%.2f, y=%.6f\n', x, y);
while x < xf
    k1 = f(x,       y          );   % Slope at start
    k2 = f(x+h/2,   y+h*k1/2  );   % Slope at midpoint (via k1)
    k3 = f(x+h/2,   y+h*k2/2  );   % Slope at midpoint (via k2, refined)
    k4 = f(x+h,     y+h*k3    );   % Slope at end (via k3)
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4);  % Weighted average of slopes
    x = x + h;
    fprintf('x=%.2f, y=%.6f\n', x, y);
end
```

**Accuracy comparison:**
| Method | Error per step | Slopes used |
|---|---|---|
| Euler | O(h²) | 1 |
| Heun's | O(h³) | 2 |
| RK4 | O(h⁵) | 4 |

RK4 is worth the extra computation — it's the standard used in most engineering/science software.

---

## ⚡ Quick Cheat Notes

| Method | Key Formula to Remember |
|--------|------------------------|
| Bisection | `c = (a+b)/2` |
| False Position | `c = b - f(b)*(b-a)/(f(b)-f(a))` |
| Jacobi | Uses old `x` for all updates |
| Seidel | Uses new `x` immediately |
| Newton Forward | Use near start; `s = (xp-x(1))/h` |
| Newton Backward | Use near end; `s = (xp-x(n))/h` |
| Lagrange | No table needed; weighted basis polynomials |
| Simpson 1/3 | `h/3 * (1,4,2,4,...,1)` — n even |
| Simpson 3/8 | `3h/8 * (1,3,3,2,3,3,...,1)` — n mult of 3 |
| Euler | `y = y + h*f(x,y)` |
| Heun's | `y = y + h*(k1+k2)/2` |
| RK4 | `y = y + h/6*(k1+2k2+2k3+k4)` |

---

*Good luck on your final! You've got this 🎯*
