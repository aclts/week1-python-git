def sum_evens(n: int) -> int:
	total = 0
	for i in range(1, n+1):
		if i%2 == 0:
			print(f"i={i}, total={total}")
			total+=i
#			print(total-2, "+2=",total)
	return total

if __name__ == "__main__":
	try:
		n = int(input("input /# > 0"))
		if n < 0:
			raise ValueError("n < 0")
		print("Sum of evens:", sum_evens(n))
	except ValueError as e:
		print(e)
