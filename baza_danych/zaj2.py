from sqlalchemy import create_engine, Column, Integer, String, text, inspect, MetaData, Table, select, func
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

metadata = MetaData()
census = Table('census',metadata, autoload_with=engine)
print(repr(census))

stmt = text('SELECT DISTINCT state FROM census')
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

print(results)

stmt1 = text('SELECT sum(pop2000) as s00, sum(pop2008) as s08 FROM census where state in ("Alaska","New York")')
result_proxy = connection.execute(stmt1)
results1 = result_proxy.fetchall()

print(results1)

stmt2 = select(
func.sum(census.c.pop2008)
).where(census.c.sex == 'F')

result_proxy = connection.execute(stmt2)
results2 = result_proxy.fetchall()
print(results2)

stmt3 = select(
func.sum(census.c.pop2008)
).where(census.c.sex == 'M')

result_proxy = connection.execute(stmt3)
results3 = result_proxy.fetchall()
print(results3)


