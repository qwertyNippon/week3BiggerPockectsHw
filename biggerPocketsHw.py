
class ROI_Cal():
    """
    Project to use in the future.
    total income, total expenses, total invested
    *** total income and total expenses --- on a month to month basis***
    ***cash flow --- income minus expenses***
    *** total invested --- how much you paid to acquire the property.***
    ***annual cash flow --- cash flow on a yearly basis***
    """   
    def __init__(self, total_income, total_expenses, total_invested):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.total_invested = total_invested

    def income_cal(self):
        inc = input(f"input your total revenue that may have been forgotten above, on a monthly basis for one or more properties. ")
        self.total_income = inc + self.total_income
        print(self.total_income)

    def exp_cal(self):
        exp = input(f"input your total expenses that may have been forgotten above, on a monthly basis for one or more properties. ")
        self.total_expenses = exp + self.total_expenses
        print(self.total_expenses)

    def cash_f(self):
        flow = self.total_income - self.total_expenses
        annual_cash = flow * 12
        print(flow)
        print(annual_cash)

    def Roi(self):
        

    

ROI_Cal(2000, 1550, 50000)