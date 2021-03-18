# Download the data
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

example1 = "data/Example1.txt"
file1 = open(example1, "r")
print(file1)

file1.name

file1.mode

fileContent = file1.read()
fileContent
print(fileContent)

type(fileContent)

file1.close

#better way to open file
with open(example1, "r") as file1:
    fileContent = file1.read()
    print(fileContent)

file1.closed
print(fileContent)

# read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

# read one line
with open(example1, "r") as file1:
    print(file1.readline())

# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()