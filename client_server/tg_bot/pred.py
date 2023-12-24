import joblib
from sklearn.preprocessing import StandardScaler
def pred_func(array):
    best_model = joblib.load('C:/Users/Yaroslav/Desktop/Heart_Attack/HeartAttack_model.joblib')
    scaler = StandardScaler()
    scaler.fit(array)
    n_array = scaler.transform(array)
    output = best_model.predict(n_array)
    return output