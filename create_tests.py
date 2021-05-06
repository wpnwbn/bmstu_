INFILE  = "test.txt"
OUTFILE = "OUT.txt"
GEN     = "gen.sh"
SCRIPT  = "run.sh"
MAIN    = "main"
DIR     = "func_test"
EXT     = ".txt"

""" INFO
INFILE - file with your test data where
 Positive test data has to be written after #+ line
 Negative test data has to be written after #- line

Example INFILE:
    #+
    [+7](926)-670-46-33
    [+8769838524698](328)-533-87-32
    #-
    [+72738749
    +79328(234)-436-74-23
    [+4] (345)-654-32-76
    [+34]32)-457-24-23
    #+
    [+43](236)-126-87-65
    #-
    [+564](765-539-35-98
    [+3567](4654)547-23-87
    [+846](765)3478-12-56
    [+685](756)234-645-87

OUTFILE - file containing all data from "*_out.txt" files.

GEN - file which will generate DIR (default: "func_test") folder with its content

SCRIPT - file which will run "*_in.txt" tests on your MAIN program and write the results
    into "*_out.txt" files and after that - copy them to OUTFILE.

MAIN - name of your executable program.
"""

with open(INFILE, "r") as infile, open(GEN, "w") as gen, open(SCRIPT, "w") as script:
    # Default test type, if there is no #+ and #- in the INFILE
    TESTTYPE = "pos"

    POS_count = 1
    NEG_count = 1

    # Headers
    script.write("#!/bin/sh\n\n")
    gen.write("#!/bin/sh\n\n")

    # Removing existing DIR directory
    gen.write(f"if [ -d ./{DIR} ]\nthen\n")
    gen.write(f"\trm -r {DIR}\n")
    gen.write(f"fi\n")
    gen.write(f"mkdir {DIR}\n")
    gen.write(f"cd {DIR}\n")

    script.write(f"cd {DIR}\n")

    i = 0
    for line in infile:

        if line[0] == '#':
            if line[1] == "+":
                TESTTYPE = "pos"
            elif line[1] == "-":
                TESTTYPE = "neg"
            continue

        if TESTTYPE == "pos":
            count = "{:02d}".format(POS_count)
            POS_count += 1
        elif TESTTYPE == "neg":
            count = "{:02d}".format(NEG_count)
            NEG_count += 1

        FILE_IN = f"{TESTTYPE}_{count}_in{EXT}" # Ex: pos_01_in.txt
        FILE_OUT = f"{TESTTYPE}_{count}_out{EXT}"

        gen.write(f'\necho "{line}" > {FILE_IN}')

        script.write(f'echo -n "{TESTTYPE.upper()}_{count}: " >{">"*(i > 0)} ../{OUTFILE}\n')
        script.write(f'../{MAIN} < {FILE_IN} > {FILE_OUT}\n')
        script.write(f'cat {FILE_OUT} >> ../{OUTFILE}\n')

        i += 1
