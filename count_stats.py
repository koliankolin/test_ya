from CounterByThreads import CounterByThreads
import sys

if __name__ == '__main__':
    counter = CounterByThreads(sys.argv[1])
    counter.get_output_file()
