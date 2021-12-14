# When I work Coding Challenge

The PageView constructor basically takes the default path as 'https://public.wiwdata.com/engineering-challenge/data/' where all the csv files are located. 
We can change the argument to the constructor to take any location, but it assumes that the files names are alphabet csv files. 
we also create the name of the output.csv file and merge.csv file when all the a.csv...... to z.csv are merged. 
And the output file consists of the format in which the code output has to be. 

to Execute the code , check out or download the file and 
run the python script using the command 

## python PageView.py 

from the directory in which the file is located and it will create two files, merge.csv which is the big file from concatinating all the csv's. 
And the Output.csv which is the file output which is desired. 

See the sample output to run the script.

(turi) Achilles:wheniwork anand$ pwd
/Users/anand/myData/wheniwork<br>

(turi) Achilles:wheniwork anand$ ll<br>
total 12328<br>
-rw-r--r--  1 anand  staff     1976 Dec 14 02:46 PageView.py<br>
-rw-r--r--  1 anand  staff  5360281 Dec 14 01:39 merge.csv<br>
drwxr-xr-x  5 anand  staff      160 Dec 14 01:53 package<br>
-rw-r--r--  1 anand  staff      327 Dec 14 02:27 test.py<br>

## (turi) Achilles:wheniwork anand$  python PageView.py 

(turi) Achilles:wheniwork anand$ ll<br>
total 12888<br>
-rw-r--r--  1 anand  staff     1976 Dec 14 02:46 PageView.py<br>
-rw-r--r--  1 anand  staff  5360281 Dec 14 02:49 merge.csv<br>
-rw-r--r--  1 anand  staff   288718 Dec 14 02:49 output.csv<br>
drwxr-xr-x  5 anand  staff      160 Dec 14 01:53 package<br>
-rw-r--r--  1 anand  staff      327 Dec 14 02:27 test.py<br>
(turi) Achilles:wheniwork anand$ <br>

The output file is also uploaded to the github


