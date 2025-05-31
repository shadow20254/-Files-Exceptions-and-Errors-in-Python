try:
    print("Reading file content:")
    a = open("sample.txt","r")
    print("Line 1:",a.readline())
    print("Line 2:",a.readline())
    a.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


