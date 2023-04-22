import numpy as np

class K_mean:
    def __init__(self, k) -> None:
        self.k = k

    def fit(self, X):
        self.centroid = X[np.random.choice(X.shape[0], self.k, replace=False)]
        store_cluster = [[] for _ in range(self.k)  ]
        for x in X:
            distance = np.sqrt( np.sum(   (x -self.centroid)**2   , axis=1)  )
            closest_cluster_idx = np.argmin(distance)
            store_cluster[closest_cluster_idx].append(x)
            self.centroid[closest_cluster_idx] = np.mean(store_cluster[closest_cluster_idx], axis=1)

    def predict(self , X_test):
        pred = []
        for x in X_test:
            distance = np.sqrt(   np.sum( (x - self.centroid)**2 , axis=1 ))
            closest_cluster_idx = np.argmin(distance)
            pred.append(closest_cluster_idx)
        return pred


if __name__ == "__main__":
    kmean  = K_mean(3)
    X_train = np.random.rand(5, 2)
    X_test =  np.random.rand(10, 2)
    kmean.fit(X_train)
    print(kmean.predict(X_test))
