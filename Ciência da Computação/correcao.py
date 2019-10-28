import os
import requests
import json

sourceCodeFileName = ""
namelistOfpublicTests = []
namelistOfoutputPublicTests = []
namelistOfoutputPrivateTests = [] 
namelistOfPrivateTests = []
count = 0
for x in os.scandir('.'):
    dirContent = []
    if (x.is_dir()):
        for y in os.scandir(x):
            dirContent.append(y.name)

        dirContent.sort()

        for x in range (len(dirContent)):
            if "py" in dirContent[x].split('.')[1]:
                sourceCodeFileName = dirContent[x]
            elif "pub" in dirContent[x].split('.')[0]:
                if dirContent[x].split('.')[1] == "in":
                    namelistOfpublicTests.append(dirContent[x])
                else:
                    namelistOfoutputPublicTests.append(dirContent[x])
            elif "pri" in dirContent[x].split('.')[0] :
                if dirContent[x].split('.')[1] == "in":
                    namelistOfPrivateTests.append(dirContent[x])
                else:
                    namelistOfoutputPrivateTests.append(dirContent[x])
        
    
        sourceCodeExtension = sourceCodeFileName.split('.')[1]
        sourceCode = open( str(count) + "/"+sourceCodeFileName, "r")
        sourceCodeContent = ""
        for linha in sourceCode:
            sourceCodeContent += linha

        code = {
            "filename": sourceCodeFileName,
            "fileextension":sourceCodeExtension,
            "filecontent": sourceCodeContent,
            "filepermission":"" 
            }
        listOfpublicTests = []
        for i in range(len(namelistOfpublicTests)):
            publicTestsFileName = namelistOfpublicTests[i]
            publicTestsFileExtension = publicTestsFileName.split('.')[1]
            publicTestsFile = open(str(i) + "/"+publicTestsFileName, "r")
            publicTestsFileContent = ""
            for linha in publicTestsFile:
                publicTestsFileContent += linha
            publicTestsData = {
                "filename": publicTestsFileName,
                "fileextension":publicTestsFileExtension,
                "filecontent": publicTestsFileContent,
                "filepermission":"" 
            }
            listOfpublicTests.append(publicTestsData)
        listOfoutputPublicTest = []
        for i in range(len(namelistOfoutputPublicTests)):
            outputPublicTestFileName = namelistOfoutputPublicTests[i]
            outputPublicTestFileExtension = outputPublicTestFileName.split('.')[1]
            outputPublicTestFile = open(str(i) + "/"+outputPublicTestFileName, "r")
            outputPublicTestFileContent = ""
            for linha in outputPublicTestFile:
                outputPublicTestFileContent += linha
            outputPublicTestData = {
                "filename": outputPublicTestFileName,
                "fileextension":outputPublicTestFileExtension,
                "filecontent": outputPublicTestFileContent,
                "filepermission":"" 
            }
            listOfoutputPublicTest.append(outputPublicTestData)
        listOfPrivateTests = []
        for i in range(len(namelistOfPrivateTests)):
            PrivateTestsFileName = namelistOfPrivateTests[i]
            PrivateTestsFileExtension = PrivateTestsFileName.split('.')[1]
            PrivateTestsFile = open(str(i) + "/"+PrivateTestsFileName, "r")
            PrivateTestsFileContent = ""
            for linha in PrivateTestsFile:
                PrivateTestsFileContent += linha
            PrivateTestsData = {
                "filename": PrivateTestsFileName,
                "fileextension":PrivateTestsFileExtension,
                "filecontent": PrivateTestsFileContent,
                "filepermission":"" 
            }
            listOfPrivateTests.append(PrivateTestsData)

        listOfoutputPrivateTest = []
        for i in range(len(namelistOfoutputPrivateTests)):
            outputPrivateTestFileName = namelistOfoutputPrivateTests[i]
            outputPrivateTestFileExtension = outputPrivateTestFileName.split('.')[1]
            outputPrivateTestFile = open(str(i) + "/"+outputPrivateTestFileName, "r")
            outputPrivateTestFileContent = ""
            for linha in outputPrivateTestFile:
                outputPrivateTestFileContent += linha
            outputPrivateTestData = {
                "filename": outputPrivateTestFileName,
                "fileextension":outputPrivateTestFileExtension,
                "filecontent": outputPrivateTestFileContent,
                "filepermission":"" 
            }
            listOfoutputPrivateTest.append(outputPrivateTestData)
        data = json.dumps({
        "id": str(count),
        "code": code,
        "pubin":listOfpublicTests,
        "pubout":listOfoutputPublicTest,
        "priin":listOfPrivateTests,
        "priout":listOfoutputPrivateTest,
        "timelimit":"3000ms"
        })
        
        arquivo = open("submissao.json", "w")
        arquivo.write(str(data))
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiUFVDTUlOQVMifQ.AY0c8T7tGdR-c-VYat-RXZRQTlUzyzNy4IwT5FZJuxk"}
        r = requests.post('http://186.248.79.46:8000', data=data, headers=headers)
        print(r.status_code)
        print(r.text)
        saida = open("saida"+str(count)+".txt", "w")
        saida.write(str(r.text))
        count = count + 1
        namelistOfpublicTests.clear()
        namelistOfoutputPublicTests.clear()
        namelistOfoutputPrivateTests.clear() 
        namelistOfPrivateTests.clear()
        listOfpublicTests.clear()
        listOfoutputPublicTest.clear()
        listOfPrivateTests.clear()
        listOfoutputPrivateTest.clear()
        
