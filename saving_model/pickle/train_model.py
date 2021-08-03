import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
name=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pd.read_csv(url,names = name)
X=df.iloc[ : , :8]
y=df.iloc[:,8]
X_train ,X_test, y_train,y_test =model_selection.train_test_split(X,y,test_size=0.2,random_state=101)
#train the model
model=LogisticRegression()
model.fit(X_train,y_train)
result=model.score(X_test,y_test)
print(result)
##Save the model
#the extensions that can be used are ('.sav'/.pkl)
pickle.dump(model,open('dib_79.pkl','wb'))