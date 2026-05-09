import pandas as pd
from database import connect

def load_data():

    conn=connect()

    df=pd.read_sql_query(
        "select * from applications",
        conn
    )

    conn.close()

    return df


def total_applicaions():

    df=load_data()

    return len(df)

def status_summary():

    df=load_data()

    return df["status"].value_counts()

def top_company():

    df=load_data()

    return df["company"].value_counts().head(1)

def success_rate():

    df=load_data()

    total=len(df)

    interviews=len(
        df[df["status"]=="Interview"]
    )

    if total==0:
        return 0
    
    return (interviews/total)*100


def export_to_csv():

    df=load_data()

    df.to_csv("applications.csv",index=False)

    print("Applications exported successfully!")