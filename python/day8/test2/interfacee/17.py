from abc import ABC, abstractmethod

# Abstract Class IDatabaseOperations
class IDatabaseOperations(ABC):
    
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, data, identifier):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass


# SQLDatabase Implementation
class SQLDatabase(IDatabaseOperations):
    
    def insert(self, data):
        print(f"Inserting {data} into SQL database.")
        # Code to insert data into SQL database

    def update(self, data, identifier):
        print(f"Updating {data} in SQL database with identifier {identifier}.")
        # Code to update data in SQL database

    def delete(self, identifier):
        print(f"Deleting record with identifier {identifier} from SQL database.")
        # Code to delete data from SQL database


# NoSQLDatabase Implementation
class NoSQLDatabase(IDatabaseOperations):
    
    def insert(self, data):
        print(f"Inserting {data} into NoSQL database.")
        # Code to insert data into NoSQL database

    def update(self, data, identifier):
        print(f"Updating {data} in NoSQL database with identifier {identifier}.")
        # Code to update data in NoSQL database

    def delete(self, identifier):
        print(f"Deleting record with identifier {identifier} from NoSQL database.")
        # Code to delete data from NoSQL database


# Example Usage
    # Using SQL Database
sql_db = SQLDatabase()
sql_db.insert({"name": "John Doe"})
sql_db.update({"name": "John Smith"}, 1)
sql_db.delete(1)

# Using NoSQL Database
nosql_db = NoSQLDatabase()
nosql_db.insert({"name": "Jane Doe"})
nosql_db.update({"name": "Jane Smith"}, 2)
nosql_db.delete(2)
