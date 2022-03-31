import os
filesList = []
   
def exploreFiles(rootPath): 
    for file in os.listdir(rootPath):
        if os.path.isfile((os.path.join(rootPath, file))):
            if file.endswith(".py"):
                filesList.append(os.path.join(rootPath, file))
        else:
            exploreFiles(os.path.join(rootPath, file))
    return filesList
