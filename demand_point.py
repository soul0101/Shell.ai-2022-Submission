import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

class DemandPoint():
    def __init__(self, index, x, y, demand_list):
        self.index = int(index)
        self.x = x
        self.y = y
        self.demand_list = demand_list
        self.demand = self.predict_demand_3()

    # def predict_demand(self):
    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
        
    #     X = x.reshape(-1, 1)
    #     y = y.reshape(-1, 1)

    #     to_predict_x= [len(x), len(x) + 1]
    #     to_predict_x= np.array(to_predict_x).reshape(-1,1)

    #     regsr=LinearRegression()
    #     regsr.fit(X,y)

    #     predicted_y= regsr.predict(to_predict_x)
    #     predicted_y = predicted_y.reshape(1, -1)
    #     return predicted_y[0]

    # def predict_demand(self):
    #     def objective(x, a, b, c):
    #         return a * x + b * x**2 + c

    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
    #     popt, _ = curve_fit(objective, x, y)
    #     a, b, c = popt

    #     return objective(np.array([len(x), len(x)+1]), a, b, c)

    def predict_demand_3(self):
        def objective(x, a, b, c):
            return a * x + b * x**3 + c

        y = np.array(self.demand_list) 
        x = np.array([i for i in range(len(y))])
        popt, _ = curve_fit(objective, x, y)
        a, b, c = popt

        return objective(np.array([len(x), len(x)+1]), a, b, c)

    def predict_demand_2(self):
        def objective(x, a, b, c):
            return a * x + b * x**2 + c

        y = np.array(self.demand_list) 
        x = np.array([i for i in range(len(y))])
        popt, _ = curve_fit(objective, x, y)
        a, b, c = popt

        return objective(np.array([len(x), len(x)+1]), a, b, c)

    def predict_demand_1(self):
        def objective(x, a, b):
            return a * x + b

        y = np.array(self.demand_list) 
        x = np.array([i for i in range(len(y))])
        popt, _ = curve_fit(objective, x, y)
        a, b = popt

        return objective(np.array([len(x), len(x)+1]), a, b)

    def predict_demand(self):
        y = np.array(self.demand_list) 
        diff = y[-1] - y[-2]
        if  diff < 0:
            return self.predict_demand_1()
        elif diff > 12:
            return self.predict_demand_2()

        return self.predict_demand_3()

    # def predict_demand(self):
    #     def objective(x, a, b, c, d, e, f):
    #         return a * x + b * x**2 + c * x**3 + d * np.sin(e * x) + f

    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
    #     popt, _ = curve_fit(objective, x, y)
    #     a, b, c, d, e, f= popt

    #     return objective(np.array([len(x), len(x)+1]), a, b, c, d, e, f)

    # def predict_demand(self):
    #     def objective(x, a, b, c, d):
    #         return a * x + b * x**2 + c * x**3 + d

    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
    #     popt, _ = curve_fit(objective, x, y)
    #     a, b, c, d = popt

    #     return objective(np.array([len(x), len(x)+1]), a, b, c, d)

    # def predict_demand(self):
    #     def objective(x, a, b, c, d, e, f):
    #         return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
    #     popt, _ = curve_fit(objective, x, y)
    #     a, b, c, d, e, f = popt

    #     return objective(np.array([len(x), len(x)+1]), a, b, c, d, e, f)

    # def predict_demand(self):
    #     def objective(x, a, b):
    #         return (a * x) + b

    #     y = np.array(self.demand_list) 
    #     x = np.array([i for i in range(len(y))])
    #     popt, _ = curve_fit(objective, x, y)
    #     a, b = popt

    #     return objective(np.array([len(x), len(x)+1]), a, b)