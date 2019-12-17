from queue import Queue
from threading import Thread
import itertools
from pathlib import Path
import time

class CounterByThreads:
    def __init__(self, file_name, chunk_size=10000):
        super().__init__()
        self.file_name = file_name
        self._chunk_size = chunk_size
        self._sum_total = 0
        self._count_total = 0
        self._count_lucky = 0

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        file_path = Path(file_name)
        if file_path.is_file():
            self.__file_name = file_name
        else:
            print(f'{file_name} does not exist')
            exit(1)

    @staticmethod
    def _convert_line_to_list(line: str) -> list:
        return [int(char) for char in line]

    @staticmethod
    def _is_lucky(numbers: list) -> bool:
        return sum(numbers[:3]) == sum(numbers[3:])

    @staticmethod
    def _is_valid_line(line: str) -> bool:
        return len(line) == 6

    def _write_stats_for_chunk_to_queue(self, chunk: list):
        for line in chunk:
            line = line.strip()
            if self._is_valid_line(line):
                try:
                    numbers = self._convert_line_to_list(line)
                except ValueError:
                    print('Line has a char symbol. Final result will be without that line')
                    continue
                if self._is_lucky(numbers):
                    self._count_lucky += 1
                self._sum_total += sum(numbers)
                self._count_total += len(numbers)
            else:
                print('Line has invalid length. Final result will be without that line')

    def _write_stats_from_file_by_chunks(self):
        threads = []
        with open(self.file_name, 'r') as f:
            while True:
                lines = list(itertools.islice(f, self._chunk_size))
                thread = Thread(target=self._write_stats_for_chunk_to_queue, args=(lines,))
                thread.start()
                threads.append(thread)
                if not lines:
                    break
        for thread in threads:
            thread.join()

    def get_output_file(self, file_name='output.txt'):
        self._write_stats_from_file_by_chunks()
        with open(file_name, 'w') as f:
            f.write(f'{self._count_lucky}\n{round(self._sum_total / self._count_total, 2)}\n')



