import redshift_connector
import json
import configparser
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
class CustomerData:
   conn=None
   def __init__(self,config:configparser,mode:str="Development"):
      self.dbconnect(config[mode])

   def getcustomerdata(self,customerid:str)->tuple:  
         # Create a Cursor object
         cursor = self.conn.cursor()
         # Query a table using the Cursor
         cursor.execute(f"select * from customer_traits where customer_id={customerid}")
         #Retrieve the query result set
         result: tuple = cursor.fetchall()
         cursor.close()
         return result
   
   def getcustomers(self,rowlimit:int)->tuple:
      # Create a Cursor object
      cursor = self.conn.cursor()
      # Query a table using the Cursor
      cursor.execute(f"select customer_id,first_name+' '+last_name as name,datediff(year,birth_date,current_date) as age,email,loyalty_level,to_char(total_purchases,'99999.99'),is_active from customer where age> 20 limit {rowlimit}")
      #Retrieve the query result set
      result: tuple = cursor.fetchall()
      cursor.close()
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
      self.conn.close()