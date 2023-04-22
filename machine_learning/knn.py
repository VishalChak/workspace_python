import numpy as np
class Knn:
    def __init__(self, k) -> None:
        self.k = k

    def fit(self, X, y):
        self.X = X
        self.y = y


    def predict(self , X_test):
        y_pred = []
        for x in X_test:
            distances = np.sqrt(np.sum ( (x-self.X)**2 , axis=1 ))
            nn_indices = np.argsort(distances)[:self.k]
            nn_labels = self.y[nn_indices]
            y_pred.append(np.bincount(nn_labels).argmax())
        return y_pred


if __name__ == "__main__":
    X_train  = np.random.rand(50,2)
    y_train = np.random.randint(0, 5 , 50)
    
    X_test = np.random.rand(1,2)
    
    knn = Knn(3)
    knn.fit(X_train, y_train)
    print(knn.predict(X_test))