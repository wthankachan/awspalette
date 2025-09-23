import redshift_connector
import json
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
class CustomerData:
   conn=None
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
      

