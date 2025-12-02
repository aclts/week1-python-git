import pandas as pd

df = pd.DataFrame({"number": range(1,11)})
df["square"] = df["number"]**2

df.to_csv("squares_pd.csv", index=False)

df2 = pd.read_csv("squares_pd.csv")

print(f"Mean square 1: {df2['square'].mean()}")

count=0
total=0
for x in df2["square"]:
	count+=1
	total+=x
print(f"Mean square 2: {total/count}")
	
