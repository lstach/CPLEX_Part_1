
from docplex.mp.model import Model

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



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
