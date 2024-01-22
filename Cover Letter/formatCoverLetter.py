file = open("CoverLetter.md")
inputFile = file.read()
inputFile = inputFile.replace("[Date]", "January 18th")
inputFile = inputFile.replace("[NameOfEmployer]", "TestCompany")
inputFile = inputFile.replace("[HRName]", "Dave")
inputFile = inputFile.replace("[SelfPresent]", "I am cole.")
inputFile = inputFile.replace("[HowDidFind]", "I just found you.")
inputFile = inputFile.replace("[ExplainReleventSkills]", "I used bash to format this letter.")
inputFile = inputFile.replace("[ExplainAchivements]", "I ran a marathon.")
inputFile = inputFile.replace("[WhyBestChoice]", "This is a Test.")
inputFile = inputFile.replace("[Closing]", "I am done")

print(inputFile)

newFile = open("NewCoverLetter.md", "w")

newFile.write(inputFile)

