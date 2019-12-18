from CounterByThreads import CounterByThreads
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('There must be at least one file as arg')
        exit(1)
    counter = CounterByThreads(sys.argv[1])
    counter.get_output_file()
