
from docplex.mp.model import Model
import docplex


# Step 2: Set up the prescriptive model #

# Create the model
m = Model(name='telephone_production')

# Define the decision variables
# continuous variable 'desk' represents production of desk telephones, 'cell' production of cell phones.
desk = m.continuous_var(name = 'desk')
cell = m.continuous_var(name='cell')

# Set up the constraints

# desk and cell phone must both be >=100, as described in the problem

# constraint 1: desk production is >= 100
m.add_constraint(desk >= 100)
# constraint 2: cell production is >= 100
m.add_constraint(cell >= 100)


# can only spend at most 400 hours on assembly and 490 hours on painting.
# presumably, each desk takes 0.2 hours to assemble and 0.5 hours to paint, while cell phones take
# 0.4 hours to assemble and paint.  but again, this wasn't described in the problem. just inferred.

# constraint 3: assembly time limit
assemblyConstraint = m.add_constraint(0.2 * desk + 0.4 * cell <= 400)

# constraint 4: painting time limit
paintingConstraint = m.add_constraint(0.5 * desk + 0.4 * cell <= 490)

# .add_constraint returns the newly-added constraint.  I'm not sure what, in real terms, this actually is, and how it differs from not assigning the returned value to anything.

# our objective is to maximize the expected revenue
m.maximize(12 * desk + 20 * cell)
# dunno where the 12 * desk and 20 * cell come from.  presumably, it's the revenue per each desktop and cellphone sold, respectively

m.print_information()
print(assemblyConstraint)
print("\n")
s = m.solve()
m.print_solution()
print("\n")

'''
This section deals with infeasability in LP:
'''
infeasibleModel = m.copy()

infeasibleDesk = infeasibleModel.get_var_by_name('desk')

infeasibleModel.add_constraint(infeasibleDesk >= 1100)

infeasibleSolution = infeasibleModel.solve()

if infeasibleSolution is None:
    print("The model is infeasible.\n")

# implement soft constraint model




# changed the RHS of the assembly constraint from 400 to 440 (accounting for overtime)
# really, the overtime variable doesn't need to be defined here.  It just represents the overtime for assembly found in the documentation when
# relaxing the constraints

#this chunk isn't really working, and I'm not sure why.  The tutorial uses the original model to relax the constraints, which doesn't
# really solve the infeasibility problem, because it doesn't relax the constraints of the infeasible model.  I'm curious what relaxing of constraints I can add
# to the provided infeasible model to make it feasible.

overtime = m.continuous_var(name='overtime', ub=40)
assemblyConstraint.rhs = 400 + overtime
m.maximize(12*desk + 20 * cell - 2 * overtime)
solution2 = m.solve()
m.print_solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
