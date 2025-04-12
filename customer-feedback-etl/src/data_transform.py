import pandas as pd
from textblob import TextBlob

def transform_data(df):
    """
    Transforms the raw data by cleaning and performing sentiment analysis.

    Args:
        df (DataFrame): Raw data.

    Returns:
        DataFrame: Processed data.
    """
    try:
        if 'Tweet' in df.columns:
            df.rename(columns={'Tweet': 'feedback'}, inplace=True)
            
        df['cleaned_feedback'] = df['feedback'].apply(clean_feedback)
        df['sentiment'] = df['cleaned_feedback'].apply(analyze_sentiment)
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

def clean_feedback(feedback):
    """Cleans the feedback text."""
    return feedback.lower().strip()

def analyze_sentiment(feedback):
    """Analyzes sentiment using TextBlob."""
    analysis = TextBlob(feedback)
    return analysis.sentiment.polarity