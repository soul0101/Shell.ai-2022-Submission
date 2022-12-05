# Shell.ai-2022-Submission [Team Disruptor]

## Top 20 General Edition / Top 4 University Edition

ToDo: 
1) Clean the code 
2) Make pipelines and classes

The main throught process of this solution can be divided into 2 parts: 
1) Prediction of 2019 and 2020 demand data
2) Optimal allocation of demand from each demand point to EV charging stations. 

The first part was done my considering an objective function ax^3 + bx^2 + cx + d and using 
curve fitting to fit a curve to the existing trend and predict demands for 2019 and 2020. 

The second part is done by modelling a cost minimization problem using Gurobi in python. 

The variables are set up as: 
 1) num_fcs: Number of Fast Charging Stations for each supply_point (Integers)
 2) num_scs: Number of Slow Charging Stations for each supply_point (Integers)
 3) Allocation Matrix - Amount of demand of demand_point i supplied by supply_point j (Float)

The constraints are: 
 1) For supply_point i num_fcs_i + num_scs_i <= num_parking_spots_i
 2) Demand supplied by each supply point <= Total possible supply for that supply point
 
The cost function is: 
 1) Sum of cost of dissatisfaction
 2) 25 * cost of demand_mismatch
 3) 600 * cost of infra

Objective is: Minimize (allocation matrix, num_fcs, num_scs) [Cost Function]

Tools Used: Python, Gurobi
