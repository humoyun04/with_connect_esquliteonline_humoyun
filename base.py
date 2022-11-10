import sqlite3 

with sqlite3.connect("talabalar.db") as test:
    cursor = test.cursor()
    cursor.executescript('''
        CREATE TABLE studentlar(
            Id INT,
            Ism TEXT,
            Yosh INT,
            Univer TEXT
        );
   
        INSERT INTO studentlar VALUES(
            '1',
            'Humoyun',
            '18',   
            'Tatu'
        );

        INSERT INTO studentlar VALUES(
            '2',
            'Azamat',
            '18',
            'Mgimo'
        );

        INSERT INTO studentlar VALUES(
            '3',
            'Mirafzal',
            '18',
            'tuit'
        );
    ''')


cursor.execute('''
    UPDATE studentlar SET Ism = 'Asilbek',Yosh = '16' WHERE Id=1;
''')

cursor.execute('''
    SELECT * FROM studentlar;
''')
print(cursor.fetchall())
