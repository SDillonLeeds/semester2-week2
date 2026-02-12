"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    cursor = conn.cursor();
    cursor.execute(f"""
SELECT films.title, screenings.screen, tickets.price FROM (
    Tickets JOIN
    Screenings ON (Screenings.screening_id=Tickets.screening_id) JOIN
    Films ON (Films.film_id=Screenings.film_id)
) WHERE (Tickets.customer_id={customer_id})
ORDER BY films.title ASC;
    """);
    return cursor.fetchall();


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    cursor = conn.cursor();
    cursor.execute("""
SELECT Screenings.screening_id, Films.title, Count(Tickets.ticket_id) AS tickets_sold FROM (
    Films JOIN
    Screenings ON (Films.film_id=Screenings.film_id) LEFT JOIN
    Tickets ON (Screenings.screening_id=Tickets.screening_id)
) GROUP BY Screenings.screening_id
ORDER BY tickets_sold DESC;
    """);
    return cursor.fetchall();


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    cursor = conn.cursor();
    cursor.execute(f"""
SELECT Customers.customer_name, SUM(Tickets.price) AS total_spent FROM (
    Customers JOIN
    Tickets ON (Customers.customer_id=Tickets.customer_id)
) GROUP BY Customers.customer_id
ORDER BY total_spent DESC LIMIT {limit};
    """);
    return cursor.fetchall();