
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(
    'user',
    '123546',
    '192.168.0.210',
    3306,
    'databases'
)

print(SQLALCHEMY_DATABASE_URI)
