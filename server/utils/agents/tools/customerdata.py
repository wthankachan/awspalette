import redshift_connector
import json
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
class CustomerData:
   conn=None
   rowlimit=10
   def __init__(self):
      self.conn = redshift_connector.connect(
         host='default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com',
         database='anycompany_customer360',
         port=5439,
         user='awspalette',
         password='awsPale733'
      )
   def getcustomerdata(self,customerid:str)->tuple:  
         # Create a Cursor object
         cursor = self.conn.cursor()
         # Query a table using the Cursor
         cursor.execute("select * from customer_traits where customer_id={customerid}")
         #Retrieve the query result set
         result: tuple = cursor.fetchall()
         cursor.close()
         return result
   def getcustomers(self)->tuple:
      # Create a Cursor object
      cursor = self.conn.cursor()
      # Query a table using the Cursor
      cursor.execute(f"select customer_id,last_name,first_name,email,loyalty_level,total_purchases,is_active from customer limit {self.rowlimit}")
      #Retrieve the query result set
      result: tuple = cursor.fetchall()
      cursor.close()
      return result 
      

