import redshift_connector
import json
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
class customerdata:
   conn=None
   def __init__(self):
      self.conn = redshift_connector.connect(
         host='default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com',
         database='anycompany_customer360',
         port=5439,
         user='awspalette',
         password='awsPale733'
      )
   def getcustomerdata(self)->tuple:  
         # Create a Cursor object
         cursor = self.conn.cursor()
         # Query a table using the Cursor
         cursor.execute("select * from customer_traits")
         #Retrieve the query result set
         result: tuple = cursor.fetchall()
         return self.formatresults(result)
   def formatresults(self,inputvalue:tuple)->tuple:
      outputvalue = inputvalue
      return outputvalue

