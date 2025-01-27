import pandas as pd
from typing import List
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,ConfusionMatrixDisplay

pd.set_option('display.max_columns', None)

def target_encode_categorical_features(
        df: pd.DataFrame, 
        categorical_columns: List[str], 
        target_column: str) -> pd.DataFrame:
    
    encoded_data = df.copy()

    for col in categorical_columns:
        encoded_data[col] = encoded_data[col].astype('category')
        encoded_data[col] = encoded_data[col].cat.codes

    return encoded_data

def impute_and_scale_data(df_features: pd.DataFrame) -> pd.DataFrame:
    imputer = SimpleImputer(strategy='mean')
    X_preprocessed = imputer.fit_transform(df_features.values)

    scaler = StandardScaler()
    X_preprocessed = scaler.fit_transform(X_preprocessed)

    return pd.DataFrame(X_preprocessed,columns=df_features.columns)


data = pd.read_csv('weather.csv')
data['RainTomorrow'] = data['RainTomorrow'].map({"No":0,"Yes":1})
data = data.iloc[:,2:]

data_1 = target_encode_categorical_features(data,["Location","WindGustDir","WindDir9am","WindDir3pm","RainToday"],"RainTomorrow")

X = data_1.drop(columns="RainTomorrow")
y = data_1["RainTomorrow"]

X = X.drop(columns=["Evaporation","Sunshine","Cloud3pm"])

data_2 = impute_and_scale_data(X)


X_train, X_test, y_train, y_test = train_test_split(data_2,y,random_state=42)

clf = RandomForestClassifier(
    max_depth=2,
    n_estimators=5,
    random_state=42
)

clf.fit(X_train,y_train)

# Calculate predictions
y_pred = clf.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
# Calculate precision
precision = precision_score(y_test, y_pred)
# Calculate recall
recall = recall_score(y_test, y_pred)
# Calculate f1 score
f1 = f1_score(y_test, y_pred)


with open("results.txt",'w') as file:
    file.write( f"accuracy:{accuracy}")
#     f'''accuracy:{accuracy}
# precision:{precision}
# recall:{recall}
# f1:{f1}
#     ''')

aea = ConfusionMatrixDisplay.from_estimator(clf,X_test,y_test)
aea.figure_.savefig("graph.png")

