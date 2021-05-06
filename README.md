# Info

`INFILE` - file with your test data where
 - Positive test data has to be written after #+ line
 - Negative test data has to be written after #- line

`OUTFILE` - file containing all data from "*_out.txt" files.

`GEN` - file which will generate DIR (default: "func_test") folder with its content

`SCRIPT` - file which will run "*_in.txt" tests on your MAIN program and write the results into "*_out.txt" files and after that - copy them to OUTFILE.

`MAIN` - name of your executable program.

# How to run
```bash
$ python create_tests.py
$ chmod +x *.sh
$ ./{GEN}          # Substitute here name of GEN file
$ ./{SCRIPT}       # Substitute here name of SCRIPT file
```
Open `{OUTFILE}` with any text editor.
