daily_sales = [4,3,4,5,6,7,9]

sum_of_all = sum(sale for sale in daily_sales if sale > 5) 
print(f"sum in generators", sum_of_all)