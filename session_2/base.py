import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_results(db, query:str) -> list[list[str]]:
    cursor = db.execute(query);
    return [list(row) for row in cursor];


def Q2P5(db):
    query:str = """
SELECT email, SUM(total_amount) FROM (
    Customers JOIN Orders ON (Customers.customer_id=Orders.customer_id)
) GROUP BY email ORDER BY total_amount DESC LIMIT 5;
    """
    print(get_results(db, query));

def Q2P6(db):
    query:str = """
SELECT category, COUNT(order_id) AS numberOfOrders FROM (
    Order_Items JOIN Products ON (Order_Items.product_id=Products.product_id)
) GROUP BY category;
    """
    df = pd.read_sql_query(query, db);
    ax = df.plot(
        kind="bar",
        x="category",
        y="numberOfOrders",
        title="Number of orders in specific states."
    );
    plt.xticks(fontsize=10, rotation=20);
    figure = ax.get_figure();
    figure.savefig("/workspaces/semester2-week2/session_2/plot.2.6.png");


def Q2P7(db):
    query:str = """
SELECT AVG(quantity) AS averageOrderQuantity FROM Order_Items;
    """
    print(get_results(db, query));

def Q2P8(db):
    query:str = """
SELECT delivery_status, COUNT(delivery_id) AS quantity FROM Deliveries GROUP BY delivery_status;
    """
    df = pd.read_sql_query(query, db);
    ax = df.plot(
        kind="pie",
        labels=df['delivery_status'].values,
        y="quantity",
        autopct="%1.1f%%",
        title="Number of orders in specific states."
    );
    plt.legend(
        loc="center left",
        fontsize='small',
        bbox_to_anchor=(1.0, 1.0)
    );
    figure = ax.get_figure();
    figure.savefig("/workspaces/semester2-week2/session_2/plot.2.8.png");


def main():

    db = get_connection()

    
    #Q2P5(db);
    Q2P6(db);
    #Q2P7(db);
    Q2P8(db);

    db.close()


if __name__=="__main__":
    main()
