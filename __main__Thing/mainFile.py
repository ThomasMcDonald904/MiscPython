# This is the base file
from time import perf_counter

start = perf_counter()
import secondaryFile



if __name__ == "__main__":
	print("This is the main file - main file")
else:
	print("This is not the main file - main file")

end = perf_counter()
print((end - start))