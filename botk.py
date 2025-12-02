def botk(prices, max_price, k):
	budget_deals = [x for x in prices if x < max_price]
#	return sorted(budget_deals)[:k]
	budget_deals.sort()
	return budget_deals[:k]
if __name__ == "__main__":
	prices = [45, 12, 88, 5, 23, 70, 15, 99, 10, 35]
	max_price = 40
	K = 3 # We want the 3 cheapest products that cost less than $40.
	print(botk(prices, max_price,K))
