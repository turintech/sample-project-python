import sqlite3
from textwrap import dedent


class SqlQuery:
    def __init__(self, db_path="data/chinook.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_indexes()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def create_indexes(self):
        """Create indexes once on class initialization."""
        cur = self.conn.cursor()
        cur.execute("CREATE INDEX IF NOT EXISTS idx_album_title ON Album (Title)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_album_albumid ON Album (AlbumId)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_artist_artistid ON Artist (ArtistId)")
        self.conn.commit()

    def query_album(self, name: str) -> bool:

        cur = self.conn.cursor()
        cur.execute(f"SELECT 1 FROM Album WHERE Title = '{name}'")
        return cur.fetchone() is not None

    def join_albums(self) -> list:

        cur = self.conn.cursor()
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

    def top_invoices(self) -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        cur = self.conn.cursor()

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