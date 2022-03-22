import requests
import pickle

print("Going to Download File")
DownloadFile = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
fileobj = open("Iris_Data.pkl", "wb") # writing data in file
pickle.dump(DownloadFile.text, fileobj)
fileobj.close()
print("Data writing is Done!")

print("Now going to load File")
fileobj1 = open("Iris_Data.pkl", "rb") # reading data from file
print(pickle.load(fileobj1))
fileobj1.close()
