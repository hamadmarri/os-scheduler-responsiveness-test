import sys
import os
import argparse
from timeit import default_timer as timer
import time
from threading import Thread
import multiprocessing
from random import *



def interactive(results, iterations):
	while True:
		r = randint(1, 3)
		if r == 1:
			start = timer()
			time.sleep(r)
			print("sorting")
			array = [randint(1, 10000) for j in range(0, 10000)]
			array2 = sorted(array)
			end = timer()
			results.value = results.value + (end - start) - r
		elif r == 2:
			start = timer()
			time.sleep(r)
			f = open("almarri", "r")
			print(f.read())
			f.close()
			end = timer()
			results.value = results.value + (end - start) - r
		else:
			start = timer()
			time.sleep(r)
			print("reading/writing to almarri2")
			if os.path.exists("almarri2"):
				os.remove("almarri2")
				
			f1 = open("almarri", "r")
			f2 = open("almarri2", "w")
			for line in f1:
				f2.write(line)
			
			f1.close()
			f2.close()
			end = timer()
			results.value = results.value + (end - start) - r
		
		iterations.value = iterations.value + 1
			
			
			

def prime(results, np):
	start = timer()
	is_prime = False

	for i in range(10001, 10001 * (np + 1), 2):
		is_prime = True
		for j in range(i - 1, 2, -1):
			if i % j == 0:
				is_prime = False
				break

	end = timer()
	results.value = end - start
	

def main():
	prime_threads = []
	interactive_threads = []
	prime_time = []	
	interactive_time = []
	interactive_iterations = []
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", help="number of interactive threads", type=int)
	parser.add_argument("-f", help="number of read/write files threads", type=int)
	parser.add_argument("--nf", help="number of read/write files iterations", type=int)
	parser.add_argument("-p", help="number of calculate prime threads", type=int)
	parser.add_argument("--np", help="number of calculate prime iterations", type=int)
	
	args = parser.parse_args()
	
	if args.p:
		prime_time = [0 for i in range(0, args.p)]
		
		for i in range(0, args.p):
			prime_time[i] = multiprocessing.Value("d", 0.0, lock=False)
			prime_threads.append(multiprocessing.Process(target=prime, args=(prime_time[i], args.np)))
		
		for i in range(0, args.p):
			prime_threads[i].start()
	
	
	if args.i:
		interactive_time = [0 for i in range(0, args.i)]
		interactive_iterations = [0 for i in range(0, args.i)]
		
		for i in range(0, args.i):
			interactive_time[i] = multiprocessing.Value("d", 0.0, lock=False)
			interactive_iterations[i] = multiprocessing.Value("i", 0, lock=False)
			interactive_threads.append( \
				multiprocessing.Process(target=interactive, \
				args=(interactive_time[i], interactive_iterations[i],)))
		
		for i in range(0, args.i):
			interactive_threads[i].start()
			
	
	# join and print results
	if args.p:
		for i in range(0, args.p):
			prime_threads[i].join()
	
	if args.i:
		for i in range(0, args.i):
			interactive_threads[i].terminate()
	
	print("\n")
	if args.p:	
		for i in range(0, args.p):
			print(i, "prime time: ", prime_time[i].value)
	
	if args.i:	
		for i in range(0, args.i):
			print(i, "total response time: ", interactive_time[i].value, \
			" runs: ", interactive_iterations[i].value, \
			" average: ", interactive_time[i].value / interactive_iterations[i].value)
	
	# if args.f:
	
	
	


if __name__ == "__main__":
	main()
