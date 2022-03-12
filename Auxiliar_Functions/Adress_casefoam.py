import glob

def find_casefoam(targetPattern):
    targetExtension1 = "*case.foam"
    targetExtension2 = "*.stl"
    files = glob.glob(targetPattern+targetExtension1)
    files += glob.glob(targetPattern+"**/"+targetExtension1)
    files += glob.glob(targetPattern + targetExtension2)
    files += glob.glob(targetPattern + "**/" + targetExtension2)
    print(files)


find_casefoam(input("Write the path of the main adress with / separator: "))
#example of a folder called Test: c:/Test/