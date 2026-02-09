from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

# -------------------------------
# Create Database
# -------------------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_db")
cursor.execute("USE phonepe_db")

# -------------------------------
# AGGREGATED TABLES
# -------------------------------

# aggregated_transaction
cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    name VARCHAR(100),
    count BIGINT,
    amount DOUBLE
)
""")

# aggregated_insurance
cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_insurance (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    Count BIGINT,
    Amount DOUBLE
)
""")

# aggregated_user
cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_user (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    Brand VARCHAR(100),
    Count BIGINT,
    Percentage DOUBLE
)
""")

# -------------------------------
# MAP TABLES
# -------------------------------

# map_transaction
cursor.execute("""
CREATE TABLE IF NOT EXISTS map_transaction (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_Count BIGINT,
    Transaction_Amount DOUBLE
)
""")

# map_insurance
cursor.execute("""
CREATE TABLE IF NOT EXISTS map_insurance (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Insurance_Count BIGINT,
    Insurance_Amount DOUBLE
)
""")

# map_user
cursor.execute("""
CREATE TABLE IF NOT EXISTS map_user (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Registered_User BIGINT
)
""")

# -------------------------------
# TOP TABLES
# -------------------------------

# top_transaction
cursor.execute("""
CREATE TABLE IF NOT EXISTS top_transaction (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Count BIGINT,
    Total_Amount DOUBLE
)
""")

# top_insurance
cursor.execute("""
CREATE TABLE IF NOT EXISTS top_insurance (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Count BIGINT,
    Total_Amount DOUBLE
)
""")

# top_user
cursor.execute("""
CREATE TABLE IF NOT EXISTS top_user (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    District VARCHAR(100),
    Registered_Users BIGINT
)
""")

# -------------------------------
# Commit & Close
# -------------------------------
conn.commit()
cursor.close()
conn.close()

print("✅ phonepe_db and all 9 tables created successfully")