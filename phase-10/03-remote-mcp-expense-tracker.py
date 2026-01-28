from fastmcp import FastMCP
import sqlite3

mcp = FastMCP(name="remote-expense-tracker")

DB_FILE = "expenses.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
create table if not exists expenses(
                id integer Primary Key autoincrement,
                date text not null,
                amount real not null,
                category text not null,
                sub_category text,
                note text)
""")
    conn.commit()
    conn.close()

init_db()


@mcp.tool()
def add_expense(date:str, amount:float, category:str, sub_category:str, note:str) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
Insert into expenses(date, amount, category, sub_category, note)
Values(?,?,?,?,?)
""", (date, amount, category, sub_category, note))
    conn.commit()
    conn.close()


@mcp.tool()
def list_expense(start_date:str, end_date:str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        select id, date, amount, category, sub_category, note
        from expenses
        where date between ? and ?
        order by date asc
""", (start_date, end_date))    
    rows = cursor.fetchall()
    conn.close()
    expenses = []
    for row in rows:
        expenses.append({
            "id" : row[0],
            "date" : row[1],
            "amount" : row[2],
            "category" : row[3],
            "sub_category" : row[4],
            "note" : row[5]
        })
    return expenses


@mcp.tool()
def summarize_expense(start_date: str, end_date: str, category: str = None) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    if category:
        query = """
select count(*), COALESCE(SUM(amount), 0) from expenses
        where date between ? and ?
        and category = ?
"""
    else:
        query = """
select count(*), COALESCE(SUM(amount), 0) from expenses
where date between ? and ?
"""
    cursor.execute(query, ((start_date, end_date)))
    count, total = cursor.fetchone()
    conn.close()
    return {
        "start_date" : start_date,
        "end_date" : end_date,
        "category" : category,
        "total_expenses" : count,
        "total_amount" : total
    }


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)