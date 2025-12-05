from __init__ import CONN, CURSOR

class Department:
    '''Class Department representing a row in the departments table.'''

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        '''Creates the departments table if it does not exist.'''
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        '''Drops the departments table if it exists.'''
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def save(self):
        '''Inserts the Department instance into the database and assigns its id.'''
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def create(cls, name, location):
        '''Creates a new department row and returns a Department instance.'''
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        '''Updates the database row with the instance's current attribute values.'''
        if self.id is None:
            raise ValueError("Cannot update a record that has not been saved.")
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        '''Deletes the corresponding row from the database.'''
        if self.id is None:
            raise ValueError("Cannot delete a record that has not been saved.")
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
