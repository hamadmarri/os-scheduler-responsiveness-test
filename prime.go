package main

import (
	"fmt"
	"flag"
	"time"
	"sync"
)

var wg sync.WaitGroup

func prime(results *time.Duration, seconds float64) {
	total_start_time := time.Now()
	start := time.Now()

	for i := 1000000001; time.Now().Sub(total_start_time).Seconds() < seconds; i += 2 {
		for j := i - 1; i > 2; i-- {
			if i % j == 0 {
				break
			}
		}
	}

	end := time.Now()
	*results = end.Sub(start)
	
	wg.Done()	
}

func main() {

	pFlag := flag.Int("p",  1, "number of threads")
	tFlag := flag.Float64("t",  10.0, "number of seconds")
	flag.Parse()

	var prime_time = make([]time.Duration, *pFlag, *pFlag)

	wg.Add(*pFlag)

	for i := 0; i < *pFlag; i++ {
		go prime(&prime_time[i], *tFlag)
	}

	wg.Wait()
	fmt.Println("prime_time", prime_time)
}