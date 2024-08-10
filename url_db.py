from glv_var import Global_Vars
from DB import DB
from DbObject import DbObject
from Schema import Schema

def read_env( file_path = ".env" ):
    with open( file_path, "r" ) as env_file:
        
        lines = env_file.readlines()
        data = {}
        for line in lines:
            line_arr = line.split("->")
            data[ line_arr[0] ] = line_arr[1].strip()
        return data

db_url = read_env( Global_Vars.env_file )[ "db_url" ]
print( "Debug:", db_url )
db = DB( db_url )
db.set_db( "url_red_proj" )
db.set_collection( "url_list" )

from faker import Faker 
"""
input( "Beginning Faker Sequence!" )

sample_obj = DbObject( Global_Vars.url_schema ).add( ( "url" , Faker().uri() ) ).add( ( "short_alias" , Faker().first_name_male() ) )

print( "Debug:", sample_obj )

db.insert( sample_obj )
"""
db.list_all()

alias = input("Alias: ")
print(db.get_object({"short_alias":alias}))
