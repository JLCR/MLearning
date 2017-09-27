def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    X = features_train
    Y = labels_train
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf_fit = clf.fit(X, Y)
    return clf_fit