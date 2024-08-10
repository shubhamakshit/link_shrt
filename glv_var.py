class g_var :

    root = "./"
    env_file = f"{root}.env"
    
    url_schema = {
        "url" : {
            "type" : str
        },
        "short_alias" : {
            "type" : str
         }
         }

    @staticmethod
    def read_env( file_path = ".env" ):
       with open( file_path, "r" ) as env_file:
           
           lines = env_file.readlines()
           data = {}
           for line in lines:
               line_arr = line.split("->")
               data[ line_arr[0].strip() ] = line_arr[1].strip()
           return data
    

