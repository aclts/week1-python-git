from sum_utils.sums import sum_evens

if __name__ == "__main__":
	try:
		n = int(input("input /# > 0"))
		print("Sum of evens:", sum_evens(n))
	except ValueError as e:
		print(e)
