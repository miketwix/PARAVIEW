import glob

def find_casefoam(targetPattern):
    targetExtension = "*case.foam"
    files = glob.glob(targetPattern+targetExtension)
    files += glob.glob(targetPattern+"**/"+targetExtension)
    print(files)


find_casefoam(input("Write the path of the main adress with / separator: "))
#example of a folder called Test: c:/Test/