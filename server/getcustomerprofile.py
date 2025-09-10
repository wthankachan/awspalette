import redshift_connector
#redshift://default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com:5439/dev
conn = redshift_connector.connect(
     host='default-workgroup.276361193305.us-east-2.redshift-serverless.amazonaws.com',
     database='anycompany_customer360',
     port=5439,
     user='awspalette',
     password='awsPale733'
  )
  
# Create a Cursor object
cursor = conn.cursor()

# Query a table using the Cursor
cursor.execute("select * from customer_traits")
                
#Retrieve the query result set
result: tuple = cursor.fetchall()
print(result)