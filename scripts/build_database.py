import sqlalchemy
import pandas as pd
import os

DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
database = sqlalchemy.create_engine(DATABASE_URL, connect_args={'sslmode': 'require'})

if __name__ == '__main__':
    df = pd.read_csv('../all_data_paintingsforCoen.csv')
    df.to_sql('artworks', database)
