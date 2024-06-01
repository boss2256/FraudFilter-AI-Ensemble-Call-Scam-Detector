import pandas as pd


def clean_data(data):
    # Convert negative values in 'Call Duration' to positive
    data['Call Duration'] = data['Call Duration'].abs()

    # Handle missing values
    data['Financial Loss'] = data['Financial Loss'].fillna(data['Financial Loss'].median())
    if not data['Flagged by Carrier'].mode().empty:
        data['Flagged by Carrier'] = data['Flagged by Carrier'].fillna(data['Flagged by Carrier'].mode()[0])
    else:
        data['Flagged by Carrier'] = data['Flagged by Carrier'].fillna('Unknown')
    return data
