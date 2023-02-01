def investment_portfolio(risk_tolerance, investment_goals):
    portfolio = []
    if risk_tolerance == "low":
        portfolio = ["fixed income", "real estate", "blue-chip stocks"]
    elif risk_tolerance == "medium":
        portfolio = ["fixed income", "real estate", "blue-chip stocks", "mid-cap stocks"]
    elif risk_tolerance == "high":
        portfolio = ["high-growth stocks", "emerging market stocks"]
    
    if investment_goals == "growth":
        portfolio = ["high-growth stocks", "emerging market stocks", "technology stocks"]
    elif investment_goals == "income":
        portfolio = ["fixed income", "real estate", "dividend-paying stocks"]
    
    return portfolio

risk_tolerance = "low"
investment_goals = "growth"

print("Recommended Investment Portfolio:", investment_portfolio(risk_tolerance, investment_goals))
