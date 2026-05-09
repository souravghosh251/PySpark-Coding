#Create a DataFrame from a list of tuples Code

from pyspark.sql.functions import *

emp_data = [(1,"Sourav", 5600),(2,"Rajesh",3500)]

emp_df = spark.createDataFrame(emp_data , ["id","name","salary"])

emp_df.show()