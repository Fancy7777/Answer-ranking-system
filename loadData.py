import json

trainJson =open('./QA_train.json').read()
devJson = open('./QA_dev.json').read();
testJson = open('./QA_test.json').read();

trainData = json.loads(trainJson)
devData = json.loads(devJson)
testData = json.loads(testJson)

# Lets get the data into a nicer format:
def changeToList(dataset):
    listOfQAs = []
    for qa in dataset:
        qList = qa["qa"]
        QAs = []
        for q in qList:
            QAs.append(q)
        listOfQAs.append(QAs)
    return listOfQAs

train = changeToList(trainData)
dev = changeToList(devData)
test = changeToList(testData)

# We have the questions, lets get the sentences:

def getSentList(dataset):
    listOfSentLists = []
    for qa in dataset:
        listOfSentLists.append(qa["sentences"])
    return listOfSentLists
        
trainSents = getSentList(trainData)
devSents = getSentList(devData)
testSents = getSentList(testData)