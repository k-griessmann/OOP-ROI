class ROI():

    def __init__(self, purchase_price, renovation_costs, rental_income, property_expenses, 
                 down_payment, interest_rate, mortgage_term, closing_costs, property_taxes, 
                 propoerty_insurance, monthly_rent_increase, property_appreciation_rate, selling_costs):
        self.purchase_price = purchase_price
        self.renovation_costs = renovation_costs
        self.rental_income = rental_income
        self.property_expenses = property_expenses
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.mortgage_term = mortgage_term
        self.closing_costs = closing_costs
        self.property_taxes = property_taxes
        self.property_insurance = propoerty_insurance
        self.monthly_rent_increase = monthly_rent_increase
        self.property_appreciation_rate = property_appreciation_rate
        self.selling_costs = selling_costs

    def calculate_cap_rate(self):
        monthly_cash_flow = self.rental_income - self.property_expenses
        annual_cash_flow = monthly_cash_flow * 12
        annual_mortgage_interest = (self.purchase_price + self.renovation_costs - self.down_payment) * self.interest_rate
        annual_net_operating_income = annual_cash_flow - annual_mortgage_interest - self.property_taxes - self.property_insurance
        cap_rate = annual_net_operating_income / (self.purchase_price + self.renovation_costs)
        return cap_rate
    
    def calculate_roi(self):
        expected_annual_appreciation = (self.monthly_rent_increase + self.property_appreciation_rate) * (self.purchase_price + self.renovation_costs) * 12 - self.selling_costs
        total_cash_invested = self.purchase_price + self.renovation_costs + self.closing_costs - self.down_payment
        total_return = expected_annual_appreciation + (self.calculate_cap_rate() * total_cash_invested)
        roi = (total_return / total_cash_invested) * 100
        return roi
    
purchase_price = float(input("Enter the purchase price of the property: "))
renovation_costs = float(input("Enter the estimated renovation costs: "))
rental_income = float(input("Enter the monthly rental income: "))
property_expenses = float(input("Enter the monthly property expenses: "))
down_payment = float(input("Enter the down payment amount: "))
interest_rate = float(input("Enter the mortgage interest rate: "))
mortgage_term = float(input("Enter the mortgage term in years: "))
closing_costs = float(input("Enter the closing costs: "))
annual_property_taxes = float(input("Enter the annual property taxes: "))
annual_property_insurance = float(input("Enter the annual property insurance: "))
monthly_rent_increase = float(input("Enter the expected monthly rent increase: "))
property_appreciation_rate = float(input("Enter the expected property appreciation rate: "))
selling_costs = float(input("Enter the expected selling costs: "))

rental_property = ROI(purchase_price, renovation_costs, rental_income, property_expenses, down_payment, 
                                 interest_rate, mortgage_term, closing_costs, annual_property_taxes, annual_property_insurance, 
                                 monthly_rent_increase, property_appreciation_rate, selling_costs)

roi = rental_property.calculate_roi()

print("The total ROI for this rental property is {:.2f}%".format(roi))