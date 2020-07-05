from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    kotak = []
    lingkaran = []
    segitiga = []

    for file in os.listdir("kotak"):
        img = Image.open("kotak/" + file)
        img = np.array(img)
        img = img.flatten()
        kotak.append(img)

    for file in os.listdir("lingkaran"):
        img = Image.open("lingkaran/" + file)
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    for file in os.listdir("segitiga"):
        img = Image.open("segitiga/" + file)
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)
    
    return kotak, lingkaran, segitiga

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    kotak, lingkaran, segitiga = load_dataset()
    print("[INFO] Loading Model")
    y_kotak = np.zeros(len(kotak))
    y_lingkaran = np.ones(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 2
    X = kotak + lingkaran + segitiga
    y = np.concatenate([y_kotak, y_lingkaran, y_segitiga])
    model.fit(X, y)
    return model