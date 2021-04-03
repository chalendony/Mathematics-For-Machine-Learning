
# Optimation 

Exercises  taken from web resources and texts books.

## Getting Started 
linprog() returns a data structure with these attributes:

* .con is the equality constraints residuals.

* .fun is the objective function value at the optimum (if found).

* .message is the status of the solution.

* .nit is the number of iterations needed to finish the calculation.

* .slack is the values of the slack variables, or the differences between the values of the left and right sides of the constraints.

 ** It tells me how much is left over for a particular constraint when all the constraints are satisfied. I

* .status is an integer between 0 and 4 that shows the status of the solution, such as 0 for when the optimal solution has been found.

* .success is a Boolean that shows whether the optimal solution has been found.

* .x is a NumPy array holding the optimal values of the decision variables.

