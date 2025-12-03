def sum_evens(n: int) -> int:
        if n < 0:
                raise ValueError("n < 0")
        total = 0
        for i in range(1, n+1):
                if i%2 == 0:
                        # print(f"i={i}, total={total}")
                        total+=i
#                       print(total-2, "+2=",total)
        return total
