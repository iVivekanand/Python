from concurrent.futures import ProcessPoolExecutor, as_completed

def recursive_sum(low, high, pool=None):
	if not pool:
		with ProcessPoolExecutor() as executor:
			future = recursive_sum(low, high, pool=executor)
			return sum(f.result() for f in as_completed(future))
	else:
		if high - low <= 1_000_000:
			return [pool.submit(sum, range(low, high))]
		else:
			mid = (high + low) // 2
			left = recursive_sum(low, mid, executor)
			right = recursive_sum(mid, high, executor)
			return left + right


if __name__ == "__main__":
	print(f"{recursive_sum(1, 1_000_000)}")
		