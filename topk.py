
# filter_topk.py
def topk_above_threshold(nums, k, thresh):
    """Return the top-k numbers greater than thresh, descending."""
    filtered = [x for x in nums if x > thresh]
    return sorted(filtered, reverse=True)[:k]

if __name__ == "__main__":
	nums = [3, 10, 7, 1, 33, 26, 9, 2]
	k = 4
	thresh =  10
	print(topk_above_threshold(nums, k, thresh))

