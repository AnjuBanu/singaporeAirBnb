
from src.database.crud_operations import Crud

class Delete(Crud):
    def __init__(self, conn):
        super().__init__(conn)
        self.conn=conn
        self.query=None


