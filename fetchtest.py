import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb1.sqlite')
cur = conn.cursor()

title = 'cuiyan test'
cur.execute('SELECT id FROM Album WHERE title = ? ', (title, ))
row = cur.fetchone()
print row