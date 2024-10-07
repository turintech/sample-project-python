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

        cur.execute("SELECT EXISTS(SELECT 1 FROM Album WHERE Title = ?)", (name,))
        exists = cur.fetchone()[0]
        conn.close()
        return exists

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
                    t.Name AS TrackName, (
                        SELECT a2.Title 
                        FROM Album a2 
                        WHERE a2.AlbumId = t.AlbumId
                    ) AS AlbumName, 
                    (
                        SELECT ar.Name 
                        FROM Artist ar
                        JOIN Album a3 ON a3.ArtistId = ar.ArtistId
                        WHERE a3.AlbumId = t.AlbumId
                    ) AS ArtistName
                FROM 
                    Track t
                """
            )
        )
        return cur.fetchall()

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
                """
            )
        )
        return cur.fetchall()[:10]