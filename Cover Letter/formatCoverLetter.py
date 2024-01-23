import sys

fileNameDirectory = {
    "template":"CoverLetter.md",
    "Output":"../CoverLetter.md",
    "SelfPresentation":"SelfIntro.txt",
    "howDidIFindThem":"howDidFind.txt", 
    "skills":"releventSkills.txt",
    "achievements":"achieve.txt",
    "bestChoice":"whyBestChoice.txt",
    "closing":"closing.txt"
}


file = open(fileNameDirectory["template"])
fileSelfPresent = open(fileNameDirectory["SelfPresentation"])
date = sys.argv[1]
hrName = sys.argv[2]
nameOfEmployer = sys.argv[3]
fileHowFind = open(fileNameDirectory["howDidIFindThem"])
fileSkills = open(fileNameDirectory["skills"])
fileAchieve = open(fileNameDirectory["achievements"])
fileBestChoice = open(fileNameDirectory["bestChoice"])
fileClosing = open(fileNameDirectory["closing"])

inputFile = file.read()
inputFile = inputFile.replace("[Date]", date)
inputFile = inputFile.replace("[NameOfEmployer]", nameOfEmployer)
inputFile = inputFile.replace("[HRName]", hrName)
inputFile = inputFile.replace("[SelfPresent]", fileSelfPresent.read())
inputFile = inputFile.replace("[HowDidFind]", fileHowFind.read())
inputFile = inputFile.replace("[ExplainReleventSkills]", fileSkills.read())
inputFile = inputFile.replace("[ExplainAchivements]", fileAchieve.read())
inputFile = inputFile.replace("[WhyBestChoice]", fileBestChoice.read())
inputFile = inputFile.replace("[Closing]", fileClosing.read())

print(inputFile)

newFile = open(fileNameDirectory["Output"], "w")

newFile.write(inputFile)

