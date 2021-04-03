"""
Using Pulp for optimizations:

- Nice when print the model you get expressions that are readable (TODO compare with cvopt)


"""
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import numpy as np


def resource_allocation():

    model = LpProblem(name="resource_allocation_2", sense=LpMaximize)

    # variables x and y to create other PuLP objects thatrepresent linear expressions and constraints
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)

    # use the += operator to append expressions to the model
    # tuples are used to define constrain and their names
    model += (2 * x + y <= 20, "red_constraint")
    model += (4 * x -5 * y >= -10, "blue_constraint")
    model += (-x + 2 * y >= -2, "yellow_constraint")
    model += (-x + 5 * y == 15, "green_constraint")

    # objective function
    objective = x + 2 * y

    # Alternative to expressing objective function : if not all sums i guess does not work??
    # model += lpSum([x, 2 * y])

    model += objective
    print(model)
    status = model.solve()

    # print status
    print(f"status: {model.status}, {LpStatus[model.status]}")

    # objective
    print(f"objective: {model.objective.value()}")

    # decision variables
    for var in model.variables():
        print(f"{var.name}: {var.value()}")

    # constraints
    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")





    
if __name__ == "__main__":
    resource_allocation()

