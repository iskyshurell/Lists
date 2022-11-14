import timeit
import time


if __name__ == '__main__':
	res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000)
	print(res)

	start = time.time()
	for i in range(10000):
		func = ["-".join(str(n) for n in range(100))]
	end = time.time()
	print(end - start)

	time = timeit.timeit('list(map(lambda n: "-".join([str(i) for i in range(100)]), range(1)))', number = 10000)
	print(time)

