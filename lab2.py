"""
Laboratory Work 2: Control of Program Execution
Task: Calculate the value of the alternating series Z.
Formula logic: Z = Σ ((-1)^(i-1) * X^(i-1)) / (i * (i+1)) for i from 1 to N
"""

def calculate_series(x_val, n_val):
    """
    Calculates the series sum and returns the result along with the last computed terms.
    
    Args:
        x_val (float): The base value for the numerator power.
        n_val (int): The number of terms to sum.
        
    Returns:
        tuple: (Z, last_chisl, last_znam, i)
    """
    z = 0.0
    last_chisl = 0
    last_znam = 0
    
    for i in range(1, n_val + 1):
        # Calculate numerator: X^(i-1)
        chisl = x_val ** (i - 1)
        # Calculate denominator: i * (i+1)
        znam = i * (i + 1)
        
        # Store last values for output
        last_chisl = chisl
        last_znam = znam
        
        # Calculate current term
        term = chisl / znam
        
        # Apply alternating sign: odd i -> add, even i -> subtract
        if i % 2 == 1:
            z += term
        else:
            z -= term
            
    return z, last_chisl, last_znam, i

def main():
    # Independent variables (can be changed for individual tasks)
    X = 2
    N = 10
    
    # Perform calculation
    Z, last_chisl, last_znam, i = calculate_series(X, N)
    
    # Dictionary of variables to display
    variables = {
        "X": X,
        "N": N,
        "Z": Z,
        "i": i,
        "last_chisl": last_chisl,
        "last_znam": last_znam
    }
    
    # Output values and types as required by the lab work
    print("--- Results ---")
    for name, value in variables.items():
        print(f"{name} = {value}, type: {type(value).__name__}")

if __name__ == "__main__":
    main()
git add lab2_solution.py README.md
git commit -m "feat: add solution for Lab 2 with variable type output"
git push origin main

