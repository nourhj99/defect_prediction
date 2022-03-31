import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV



df = pd.read_csv ('jm1.csv')


X = df[['uniq_Op','uniq_Opnd','total_Op','total_Opnd','l','loc','v(g)','lOComment','v','e']].to_numpy()
y = df[['defects']].to_numpy()
y= y.flatten()
X = X.tolist()
y = y.tolist()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


'''

parameters = {
    'hidden_layer_sizes': [(20,),(16),(20,16),(4),(2,4)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.1,0.01, 0.05],
    'learning_rate': ['constant','adaptive'],
}



mlp = MLPClassifier(max_iter = 1000,verbose = True,activation = 'relu',alpha = 0.1,hidden_layer_sizes = (20),learning_rate = 'constant',solver = 'adam')
mlp = GridSearchCV(mlp, parameters, n_jobs=-1, cv=5)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
print(classification_report(y_test,predictions))

print('Best parameters found:\n', mlp.best_params_)
'''

'''
parameters = {
	'n_neighbors' : [3,5,7,9,11,13,15,17,19,21,23],
	'algorithm' : ['auto','ball_tree','kd_tree','brute'],
	'leaf_size' : [10,20,30,50,70,80]
}
'''
'''
clf = KNeighborsClassifier(n_neighbors = 23,algorithm = 'brute',leaf_size = 10)
#clf = GridSearchCV(clf, parameters, n_jobs=-1, cv=5)
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)
print(classification_report(y_test,predictions))
print('Best parameters found:\n', clf.best_params_)

'''


parameters = {
	'kernel' : ['linear', 'poly', 'rbf', 'sigmoid'],
	'C' : [0.001,0.1,1]
}
print("training")
clf = SVC(verbose = True)
clf = GridSearchCV(clf, parameters, n_jobs=-1, cv=5)
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)
print(classification_report(y_test,predictions))
print('Best parameters found:\n', clf.best_params_)


'''
plt.plot(df[['v(g)']],df[['loc']],'bo')
plt.show()
'''

'''
fig = plt.figure()
  
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
  
# defining all 3 axes
z = df[['defects']]
x = df[['v(g)']]
y = df[['n']]

ax.set_xlabel('Cyclomatic Complexity')
ax.set_ylabel('Hlastead Volume')
ax.set_zlabel('Defect')  
# plotting
ax.scatter(x, y, z)
ax.set_title('3d visual for CC,Total Operations and Operands,Defect')
plt.show()
'''

'''


clf = SVC(kernel='linear',verbose = True)

clf.fit(X_train,y_train)

'''
filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))

s = clf.score(X_test, y_test)
print(s)


