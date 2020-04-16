print('working')

import numpy as np
import pandas as pd

from sklearn.cluster import KMeans

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, cross_val_predict, KFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn import linear_model
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from sklearn.metrics import confusion_matrix

print('working')

# load csv file
df = pd.read_csv('./house_data_colombo_cluster1 (1).csv')
print('working')
#Add new features
df['h_l_ratio'] = df['house_size'].apply(lambda x: x * 0.0036730945821854912)/ df['land_size']
df['Bed Size'] = df['house_size'] / df['beds']

features_important =[
    ['beds', 'baths', 'land_size','0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38' ],
    [ 'beds', 'baths','house_size', 'h_l_ratio','0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'baths', 'land_size', 'h_l_ratio', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'baths', 'land_size', 'Bed Size', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'house_size', 'land_size', 'beds_bath_ratio','0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'house_size', 'h_l_ratio', 'beds_bath_ratio', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'land_size', 'h_l_ratio', 'beds_bath_ratio', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'baths', 'house_size', 'h_l_ratio', 'beds_bath_ratio','0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'baths', 'land_size', 'h_l_ratio', 'beds_bath_ratio', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    [ 'beds', 'baths', 'h_l_ratio', 'Bed Size', 'beds_bath_ratio', '0', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
       '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38']  
]

# split dataset by price
df_range_1 = df.query('price < 2.0e7')
df_range_2 = df.query('price >= 2.0e7 & price < 4.0e7')
df_range_3 = df.query('price > 4.0e7' )

#define paramss
param_grid = { 
    'n_estimators': [20, 40, 50, 80,100, 120, 130, 150, 180, 200, 220, ],
    'max_features': [1, 2, 3, 4, 5, 6,8, 9,10,11,12,15,18,'auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8, 10,20,25],
    'criterion' :['mse', 'mae']
}

sample = {
     'n_estimators': [20, 40 ]
}

def tune_params(file_name, df, param_grid ):
    print('working')
    #split dataset
    X_train,X_test,Y_train,Y_test = train_test_split(
        df.drop(['price'], axis=1),
        df['price'],
        test_size=0.33,
        random_state=42)
    grid_search = GridSearchCV(param_grid=param_grid, estimator=RandomForestRegressor(), cv=5, scoring='r2')
    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)
    #measures
    rmse = np.sqrt(((y_pred - Y_test) ** 2).mean())
    with open(file_name, 'a') as file:
        file.write(str(rmse))
        file.write('\n')
        file.write(str(grid_search.best_estimator_))
        file.write('\n')
        file.write(str(grid_search.best_params_))
        file.write('\n')

# tune_params('range1', df_range_1, param_grid)
# tune_params('range2', df_range_2, param_grid)
# tune_params('range3', df_range_3, param_grid)
tune_params('sample.txt', df_range_3, sample)

