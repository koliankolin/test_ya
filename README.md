#### Test cases
##### Valid file with lucky numbers
```
~$ python3 count_stats.py tests/input.txt 
~$ cat output.txt
1
2.88
```
##### Valid file without lucky numbers
```
~$ python3 count_stats.py tests/input1.txt 
~$ cat output.txt
0
3.39
```
##### Invalid file with chars
```
~$ python3 count_stats.py tests/input_err_char.txt
Line has a char symbol. Final result will be without that line
Line has a char symbol. Final result will be without that line
~$ cat output.txt
0
4.17
```
##### Invalid file with wrong length
```
~$ python3 count_stats.py tests/input_err_num.txt
Line has invalid length. Final result will be without that line
~$ cat output.txt 
0
2.5
```
##### Invalid file name
```
~$ python3 count_stats.py input_err_num.txt
input_err_num.txt does not exist
~$ cat output.txt
cat: output.txt: Нет такого файла или каталога
```
