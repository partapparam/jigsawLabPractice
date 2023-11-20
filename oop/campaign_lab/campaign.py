class Campaign:
    def __init__(self, budget):
        self.budget = float(budget)

    def set_revenue(self, revenue):
        self.revenue = revenue


    def profit(self):
        return self.revenue - self.budget

    def set_customers_acquired(self, customers):
        self.customers = customers
        return
    
    def average_revenue_per_customer(self):
        return self.revenue / self.customers
    
    def breakeven_customer_number(self):
        avg_revenue = self.revenue - self.customers
        return self.budget / avg_revenue