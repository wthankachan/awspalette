import redshift_connector
import json
import configparser
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
class CustomerData:
   conn=None
   config=None
   mode="Development"
   def __init__(self,config:configparser,mode:str="Development"):
      self.config=config
      self.mode=mode


   def getcustomerdata(self,customerid:str)->tuple:  
         if self.conn is None:
            self.dbconnect(self.config[self.mode])
         # Create a Cursor object
         cursor = self.conn.cursor()
         # Query a table using the Cursor
         try:
            cursor.execute(f"select * from customer_traits where customer_id={customerid}")
         except Exception as e:
            print(f"Error occured: {e}")
            cursor.close()
            self.dbclose()
            return json.loads(f"{"Error": {e}}")
         #Retrieve the query result set
         result: tuple = cursor.fetchall()
         cursor.close()
         self.dbclose()
         return result
   
   def getcustomers(self,rowlimit:int=10)->tuple:
      if self.conn is None:
            self.dbconnect(self.config[self.mode])
      # Create a Cursor object
      cursor = self.conn.cursor()
      # Query a table using the Cursor
      try:
         cursor.execute(f"select customer_id,first_name+' '+last_name as name,datediff(year,birth_date,current_date) as age,email,loyalty_level,to_char(total_purchases,'99999.99'),is_active from customer where age> 20 limit {rowlimit}")
      except Exception as e:
            print(f"Error occured: {e}")
            cursor.close()
            self.dbclose()
            return json.loads(f"{"Error": {e}}")
      #Retrieve the query result set
      result: tuple = cursor.fetchall()
      cursor.close()
      self.dbclose()
      return result
   
   def dbconnect(self,dbconfig): 
      self.conn = redshift_connector.connect(
         host=dbconfig["host"],
         database=dbconfig["database"],
         port=dbconfig["port"],
         user=dbconfig["user"],
         password=dbconfig["password"]
      )

   def dbclose(self):
      if self.conn is None:
         return
      self.conn.close()
      self.conn=None
