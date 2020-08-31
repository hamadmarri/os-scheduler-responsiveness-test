# os-scheduler-responsiveness-test

This is a python script that tests responsiveness or interactivity of the OS scheduler.
The interactive thread sleeps more than it runs (i.e. user clicks). The script measures
interactivity with 3 different tasks (sort 10000 array, read file and print to console, read file and write it to another file). During each
process it sleeps for random time between 1s-3s. At the same time, you can run # threads doing is prime function which overwhelm the cpu which is usefull
to test the interactivity during heavy tasks running.

## Options

```
python3 responsiveness.py -h 
usage: responsiveness.py [-h] [-i I] [-f F] [--nf NF] [-p P] [--np NP]

optional arguments:
  -h, --help  show this help message and exit
  -i I        number of interactive threads
  -f F        number of read/write files threads
  --nf NF     number of read/write files iterations
  -p P        number of calculate prime threads
  --np NP     number of calculate prime iterations
```


## Example
`python3 responsiveness.py -i1 -p4 --np 2`

-i is the number of threads for interactive test, usually one or two is good as it represents a user activity

-p is the number of threads performing is prime function

--np the size of numbers in prime test:
```
 for i in range(10001, 10001 * (np + 1), 2):
 ```
 
 
 
