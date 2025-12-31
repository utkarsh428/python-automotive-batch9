from typing import Tuple

class BusinessUtility:
    def calculate_margin(self, revenue: float, cost: float) -> float:
        if revenue == 0:
            return 0.0
        return ((revenue - cost) / revenue) * 100

class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self, revenue: float, cost: float) -> float:
        regular_margin = super().calculate_margin(revenue, cost)
        return regular_margin + 10.0

class ProfitabilityChecker:
    def check_profitability(self, regular_margin: float) -> str:
        if regular_margin >= 10.0:
            return "Business is profitable."
        return "Business is not profitable."

def main() -> None:
    try:
        revenue = float(input("Enter revenue: ").strip())
        cost = float(input("Enter cost: ").strip())
        
        if revenue < 0 or cost < 0:
            print("Revenue and cost should be non-negative.")
            return
        regular_calc = BusinessUtility()
        seasonal_calc = SeasonalBusinessUtility()
        checker = ProfitabilityChecker()
        
        regular_margin = regular_calc.calculate_margin(revenue, cost)
        seasonal_margin = seasonal_calc.calculate_margin(revenue, cost)
        
        status = checker.check_profitability(regular_margin)
        
        print(f"Regular Margin = {regular_margin:.2f}%")
        print(f"Seasonal Margin = {seasonal_margin:.2f}%")
        print(status)
        
    except ValueError:
        print("Please enter valid numeric values for revenue and cost.")

if __name__ == "__main__":
    main()