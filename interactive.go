package main

import (
	"fmt"
	"time"
	"flag"
	"sort"
	"math/rand"
	"io/ioutil"
	"os"
	"log"
)

func sorting(results *time.Duration) {
	size := 100000
	ints := make([]int, size, size)

	start := time.Now()
	time.Sleep(1 * time.Second)
	
	for i := 0; i < size; i++ {
		ints[i] = rand.Intn(size)
	}

	sort.Ints(ints)
	fmt.Println(ints)

	end := time.Now()
	*results += end.Sub(start)
	*results -= (1 * time.Second)
}

func readFile(results *time.Duration) {
	start := time.Now()
	time.Sleep(2 * time.Second)

	dat, _ := ioutil.ReadFile("almarriGO")
	fmt.Println(string(dat))

	end := time.Now()
	*results += end.Sub(start)
	*results -= (2 * time.Second)
}

func readWriteFile(results *time.Duration) {
	start := time.Now()
	time.Sleep(3 * time.Second)

	fmt.Println("reading/writing to almarri2")
	os.Remove("almarri2")
	
	f, err := os.Create("almarri2")

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()
  
	bytes, _ := ioutil.ReadFile("almarriGO")
	s := string(bytes)

	_, err2 := f.WriteString(s)

    if err2 != nil {
        log.Fatal(err2)
    }

	end := time.Now()
	*results += end.Sub(start)
	*results -= (3 * time.Second)
}

func interactive(results *time.Duration, iterations *int,
					seconds float64) {
	total_start_time := time.Now()
	r := 1

	for i := 0; time.Now().Sub(total_start_time).Seconds() < seconds; i++ {

		if r == 1 {
			sorting(results)
		} else if r == 2 {
			readFile(results)
		} else {
			readWriteFile(results)
		}

		*iterations++

		r += 1
		if r > 3 {
			r = 1
		}
	}

}

func main() {
	var interactive_time time.Duration
	var interactive_iterations int
	tFlag := flag.Float64("t",  10.0, "number of seconds")
	flag.Parse()

	interactive_time = 0
	interactive(&interactive_time, &interactive_iterations, *tFlag)

	fmt.Println("total response time: ", interactive_time.Seconds(), "s")
	fmt.Println("runs: ", interactive_iterations)
	
	conv := interactive_time.Nanoseconds() / int64(interactive_iterations)
	fmt.Println("average: ", time.Duration(conv).Seconds(), "s")
}