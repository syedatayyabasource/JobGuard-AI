import pandas as pd
import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_extraordinary_model():
    print("--- Job Scam Detector: Training Intelligence Unit ---")
    
    try:
        # 1. Dataset Load Karein
        csv_file = 'fake_job_postings.csv'
        if not os.path.exists(csv_file):
            print(f"Error: {csv_file} nahi mili! Pehle CSV file check karein.")
            return

        # Dataset reading with error handling
        df = pd.read_csv(csv_file, on_bad_lines='skip', engine='python')
        
        # 2. Data Cleaning
        df.columns = df.columns.str.strip() 
        df.fillna('', inplace=True)
        
        # FIX: .str.lower() use kiya hai takay Series error na aaye
        #
        df['combined_text'] = (df['title'].astype(str) + " " + df['description'].astype(str)).str.lower()

        # 3. Advanced Vectorization
        # N-gram range (1,2) se AI patterns behtar samajhta hai
        tfidf = TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1,2))
        X = tfidf.fit_transform(df['combined_text'])
        
        # Target column (fraudulent)
        y = df['fraudulent'] if 'fraudulent' in df.columns else df.iloc[:, -1]

        # 4. Model Training (With Probability Support for Confidence Meter)
        # alpha=0.1 model ki accuracy behtar karta hai
        model = MultinomialNB(alpha=0.1)
        model.fit(X, y)

        # 5. Model aur Vectorizer ko Save karein
        pickle.dump(model, open('model.pkl', 'wb'))
        pickle.dump(tfidf, open('tfidf.pkl', 'wb'))

        print("---------------------------------------------")
        print("SUCCESS: Intelligence Model Synced!")
        print(f"Total Patterns Learned: {X.shape[1]}")
        print("---------------------------------------------")

    except Exception as e:
        print(f"SYSTEM ERROR during training: {e}")

if __name__ == "__main__":
    train_extraordinary_model()