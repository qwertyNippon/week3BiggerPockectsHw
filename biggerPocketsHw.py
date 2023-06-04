
class ROI_Cal():
    """
    Project to use in the future.
    total income, total expenses, total invested
    *** total income and total expenses --- on a month to month basis***
    ***cash flow --- income minus expenses***
    *** total invested --- how much you paid to acquire the property.***
    ***annual cash flow --- cash flow on a yearly basis***
    """   
    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.total_invested = 0
        self.annual_cash = 0

    def income_cal(self):
        inc = int(input("input your total income on a monthly basis for one or more properties. "))
        self.total_income = inc
        print(self.total_income)

    def exp_cal(self):
        exp = int(input("input your total expenses on a monthly basis for one or more properties. "))
        self.total_expenses = exp 
        print(self.total_expenses)

    def cash_f(self):
        flow = self.total_income - self.total_expenses
        self.annual_cash = flow * 12
        print(flow)
        print(self.annual_cash)

    def Roi(self):
        totIn = int(input("input your total invested to acquire the property "))
        self.total_invested = totIn
        ROI = self.annual_cash / self.total_invested * 100
        print(f"Your Rate of return for this property portfolio is{ROI}%")
        print(f"The average return of the S&P500 is 10%")
        print(f"The average return of the U.S overall stock market is 8%")
        print(f"the average return of 401Ks and pension funds are 7%")

    def run(self):
        self.income_cal()
        self.exp_cal()
        self.cash_f()
        self.Roi()


myrental = ROI_Cal()
myrental.run()