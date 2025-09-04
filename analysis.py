import sqlite3
import pandas as pd

def analyze_jobs():
    conn = sqlite3.connect("jobs.db")

    # Example 1: Count jobs per company
    query1 = "SELECT company, COUNT(*) as job_count FROM jobs GROUP BY company ORDER BY job_count DESC LIMIT 10"
    df1 = pd.read_sql(query1, conn)
    print("📊 Top 10 Companies by Job Count:")
    print(df1, "\n")

    # Example 2: Jobs in a specific city (e.g., Remote)
    query2 = "SELECT title, company, location FROM jobs WHERE location LIKE '%Remote%'"
    df2 = pd.read_sql(query2, conn)
    print("🌍 Remote Jobs:")
    print(df2, "\n")

    conn.close()

if __name__ == "__main__":
    analyze_jobs()
