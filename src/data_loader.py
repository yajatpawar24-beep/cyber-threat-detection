import pandas as pd

def load_data():
    """Load train, validation, and test datasets."""
    train_df = pd.read_csv('data/raw/labelled_train.csv')
    val_df = pd.read_csv('data/raw/labelled_validation.csv')
    test_df = pd.read_csv('data/raw/labelled_test.csv')
    
    print(f"Loaded - Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")
    
    return train_df, val_df, test_df