# Exercise explanations and code guide

This README explains the four Python scripts in this exercise folder and the code that was filled in where the professor left `# FILL THIS FUNCTION` markers. The explanations are written for a beginner and include the formulas, why we chose specific implementations, and how to run the scripts.

Files in this folder
- `monovariate.py` — computes the sample mean and sample variance for a small list of numbers and plots a normal PDF using those parameters.
- `bivariate.py` — computes mean, variance, covariance and correlation for two lists of numbers and plots their distributions.
- `cov2d_scatter.py` — helper functions to build a rotated 2×2 covariance matrix and to extract principal-axis angles from a covariance matrix; also generates a scatter of a 2D Gaussian.
- `cov3d_scatter.py` — example that samples a 3D multivariate normal distribution and plots a 3D scatter. (No edits required in the exercise.)

Summary of the code that was filled

1) monovariate.py
- mean(values): returns the arithmetic mean mu = (1/n) * sum_i x_i.
- variance(values): returns the unbiased sample variance sigma^2 = (1/(n-1)) * sum_i (x_i - mu)^2. The code returns 0.0 for lists of length 0 or 1 to avoid division-by-zero.

Why sample (n-1) not population (n)?
- If the numbers are a sample drawn from a larger population, dividing by (n-1) gives an unbiased estimate of the population variance. Many exercises ask for sample variance.

Edge cases handled
- empty list: mean() returns 0 and variance() returns 0.0.
- single-element list: variance() returns 0.0.

2) bivariate.py
- mean(values) and variance(values) use the same implementations as `monovariate.py`.
- covariance(values1, values2): sample covariance cov = (1/(n-1)) * sum_i (x_i - mu_x)*(y_i - mu_y). If n <= 1 returns 0.0.
- correlation_coefficient(values1, values2): r = cov / (sigma_x * sigma_y). The code returns 0.0 if either standard deviation is zero to avoid division-by-zero.

Intuition and formulas
- Covariance: measures joint variability. Positive if both variables increase together, negative if they move opposite ways.
- Correlation coefficient: normalized covariance with value between -1 and +1. It is unitless and easier to interpret.

Edge cases and notes
- If a variable has zero variance (all values identical), correlation is mathematically undefined — the code returns 0.0 to avoid crashing. In strict math you might raise an exception.
- With small sample sizes, covariance and correlation can be noisy; don't over-interpret them.

3) cov2d_scatter.py
- rot_cov(angle, scale_x, scale_y): constructs a rotated covariance matrix C = R * D * R^T where R is the 2D rotation matrix for `angle` (radians) and D = diag(scale_x, scale_y). The returned matrix represents variances scale_x and scale_y oriented by `angle`.
- extract_angles_from_cov(cov): computes eigenvectors of the covariance matrix and converts them to angles with arctan2. These angles point in the principal directions of maximum and minimum variance.

Why eigenvectors?
- A covariance matrix is symmetric positive-semidefinite. Its eigenvectors point along the principal axes and eigenvalues are the variances along those axes. Finding them tells you the orientation and spread of the Gaussian.

Edge cases
- If scale_x == scale_y (isotropic covariance), eigenvectors are not unique — the routine will return some orthogonal directions, which is expected.

How to run the scripts (PowerShell on Windows)
Each script will open a Matplotlib plot window. Close the plot window to let the script finish.

```powershell
python "<path-to-folder>\monovariate.py"
python "<path-to-folder>\bivariate.py"
python "<path-to-folder>\cov2d_scatter.py"
python "<path-to-folder>\cov3d_scatter.py"
```

Replace `<path-to-folder>` with the absolute path to this folder on your machine. Example from your workspace:
```powershell
python "c:\Users\mashw\OneDrive\Desktop\CollegeMaterials\sensor tech and sensor data fuision\codes\ProgExercise 3 - for Sheet 2-20251112\ProgExercise 3 - for Sheet 2\monovariate.py"
```

Quick checks (examples you can run interactively)
- Test mean and variance quickly in Python REPL:
```python
from monovariate import mean, variance
print(mean([1,2,3]))     # expect 2.0
print(variance([1,2,3])) # expect 1.0 (sample variance = 1/(3-1) * ((1-2)^2+(2-2)^2+(3-2)^2)=1)
```

Suggested small improvements (optional)
- Use NumPy built-ins for shorter code: np.mean(values), np.var(values, ddof=1) and np.cov for covariance. That will be faster for large arrays.
- Add unit tests (pytest) that assert known outputs for small, deterministic inputs. I can add those if you want.
- Replace returning 0 for edge cases with explicit exceptions if you want stricter behavior for incorrect inputs.

If you want, I can now:
- add unit tests using `pytest` (quick and small) and run them, or
- convert the functions to NumPy equivalents for compactness, or
- add comments/inline docstrings inside the Python files explaining each step.

---
If you'd like the README content adjusted (simpler, more detailed math, or with diagrams), tell me how you'd like it and I will update the file.

