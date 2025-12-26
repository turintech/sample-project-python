import sqlite3
from textwrap import dedent

class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM Album WHERE Title = ?", (name,))
        result = cur.fetchone()
        conn.close()
        return result is not None

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        cur.execute(
            dedent(
                """\
                SELECT 
                    t.Name AS TrackName, 
                    a2.Title AS AlbumName, 
                    ar.Name AS ArtistName
                FROM 
                    Track t
                JOIN Album a2 ON a2.AlbumId = t.AlbumId
                JOIN Artist ar ON ar.ArtistId = a2.ArtistId
                """
            )
        )
        result = cur.fetchall()
        conn.close()
        return result

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        cur.execute(
            dedent(
                """\
                SELECT 
                    i.InvoiceId, 
                    c.FirstName || ' ' || c.LastName AS CustomerName, 
                    i.Total
                FROM 
                    Invoice i
                JOIN Customer c ON c.CustomerId = i.CustomerId
                ORDER BY i.Total DESC
                LIMIT 10
                """
            )
        )
        result = cur.fetchall()
        conn.close()
        return result