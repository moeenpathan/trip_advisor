import pandas as pd
import pymysql
import mysql.connector
from sqlalchemy import create_engine

def read_file(path):
    """ This functions taken path as input and return dataframe"""
    df = pd.read_csv(path)
    return df


def drop_fun(df):
    """ This functions taken df as input and 
        drop null values and
        return dataframe"""
    df = df.drop_duplicates()
    df = df.dropna() #drop nan rows if present
    return df


def rename_cols(df, col_list):
    """ This functions taken df as input.
    rename columns 
    and return dataframe"""
    ''' Renaming column names'''
    df.columns = col_list
    return df


def balacning_date(df):
    df = df.str.replace('/','-')    #replacing the / with -  for correct date time format
    df = pd.to_datetime(df, errors='coerce')
   
    return df


def converting_dollar(df):
    
    df = df.str.replace(r'$','').str.replace(r',','').str.replace(r' ','').str.replace(r'USD','').astype(float)
    df = df.apply(lambda x : x*82)
    
    return df


def add_new_col_mapping(df,source_col,new_col,dict1):
    df[new_col] = df[source_col].replace(dict1)    
    return df


def get_db_connection(schema):

    user_name = 'root'
    password = 'MCdonalds1'
    host = 'localhost'
    port = 3306

    conn = create_engine(f'mysql+mysqlconnector://{user_name}:{password}@{host}:{port}/{schema}')
    return conn


def load_table(df,table_name,conn):

    df.to_sql(table_name, con = conn, if_exists='append', index = False, chunksize=50)

    print(f'table {table_name}  loaded successfully to database')

if __name__ == "__main__":

    ''' Reading File'''
    file_path = r"C:\Users\Acer\Desktop\Project\apka_trip_wala.csv"
    trip_df = read_file(file_path)

    ''' Removing Na values'''
    trip_df = drop_fun(trip_df)

    table_col_list = ['Trip_ID', 'Destination', 'Start_date', 'End_date', 'Duration','Traveler_name','Traveler_age','Traveler_gender','Traveler_nationality','Accommodation_type','Accommodation_cost','Transportation_type','Transportation_cost']
    trip_df = rename_cols(trip_df, table_col_list)


    trip_df['Start_date'] = balacning_date(trip_df['Start_date'])
    trip_df['End_date'] =  balacning_date(trip_df['End_date'])

    trip_df['Accommodation_cost'] = converting_dollar(trip_df['Accommodation_cost'])
    trip_df['Transportation_cost'] =  converting_dollar(trip_df['Transportation_cost'])


    accom_dict1 =   {'Hotel' : 1,'Resort': 2,'Villa': 3,'Hostel': 4,'Airbnb': 5,'Riad': 6,'Guesthouse': 7,'Villa': 8,'Vacation rental': 9}
    trip_df = add_new_col_mapping(trip_df,'Accommodation_type','Accommodation_type_id',accom_dict1 )

    tranp_dic1 = {'Airplane' : 1,'Bus': 2,'Car' : 3,'Car rental': 4,'Ferry': 5,'Flight': 6,'Plane': 7,'Subway': 8,'Train': 9,'flight': 6}
    trip_df = add_new_col_mapping(trip_df,'Transportation_type','Transportation_type_id',tranp_dic1)

    conn = get_db_connection('trip_advisor')

    load_table(trip_df,"travel_details", conn)