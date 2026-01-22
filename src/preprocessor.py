from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(train_df, val_df, test_df):
    """Separate features/labels and scale the data."""
    
    # Separate features and labels
    X_train = train_df.drop('sus_label', axis=1).values
    y_train = train_df['sus_label'].values
    X_test = test_df.drop('sus_label', axis=1).values
    y_test = test_df['sus_label'].values
    X_val = val_df.drop('sus_label', axis=1).values
    y_val = val_df['sus_label'].values
    
    # Scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    X_val = scaler.transform(X_val)
    
    # Save scaler for later use
    joblib.dump(scaler, 'models/scaler.pkl')
    print("Saved scaler to models/scaler.pkl")
    
    return X_train, y_train, X_val, y_val, X_test, y_test, scaler