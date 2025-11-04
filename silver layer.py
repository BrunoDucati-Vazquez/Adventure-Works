# Databricks notebook source
# MAGIC %md
# MAGIC ### **Silver Layer Script**

# COMMAND ----------

# MAGIC %md
# MAGIC # Data access using app

# COMMAND ----------



spark.conf.set("fs.azure.account.auth.type.datalakeengproject01bdv.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.datalakeengproject01bdv.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.datalakeengproject01bdv.dfs.core.windows.net", "")
spark.conf.set("fs.azure.account.oauth2.client.secret.datalakeengproject01bdv.dfs.core.windows.net", "")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.datalakeengproject01bdv.dfs.core.windows.net", "https://login.microsoftonline.com/be4b9206-5bf8-46e8-89f4-03478cbe031d/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Data loading**

# COMMAND ----------

df_Calendar = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_Customers = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_Product_Categories = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Product_Categories')

# COMMAND ----------

df_Products = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_Returns = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Returns')

# COMMAND ----------

df_Sales = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_Territories = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

df_Product_Subcategories = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@datalakeengproject01bdv.dfs.core.windows.net/Product_Subcategories')

# COMMAND ----------

# MAGIC %md
# MAGIC # **Transformations**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Frame Calendars Transformations**

# COMMAND ----------

df_Calendar.display()

# COMMAND ----------

# Extract the month and year and put into separated columns

df_Calendar = df_Calendar.withColumn('Month', month(df_Calendar.Date))
df_Calendar = df_Calendar.withColumn('Year', year(df_Calendar.Date))
df_Calendar.display()

# COMMAND ----------

df_Calendar.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Calendar")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Frame Customers Transformations**

# COMMAND ----------

df_Customers.display()

# COMMAND ----------

# Creating an column called full name, which is concatetation of Prefix + FirstName + LastName

df_Customers = df_Customers.withColumn('Full_Name', concat(df_Customers.Prefix, df_Customers.FirstName, df_Customers.LastName))

df_Customers.display()

# COMMAND ----------

# Change the EmailAddress to be FirstName + LastName@adventure-works.com

df_Customers = df_Customers.withColumn('EmailAddress', concat(lower(df_Customers.FirstName),lit(".") ,lower(df_Customers.LastName), lit('@adventure-works.com')))

df_Customers.display()

# COMMAND ----------

# Change the format of the BirthDate from yyyy-MM-dd to dd-MM-yyyy

df_Customers = df_Customers.withColumn('BirthDate', date_format(df_Customers.BirthDate, 'dd-MM-yyyy'))


# COMMAND ----------

df_Customers.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Customers/")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Frame Sub Categories Transformations**

# COMMAND ----------

df_Product_Subcategories.display()

# COMMAND ----------

df_Product_Subcategories.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/Subcategories")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Products Transformations

# COMMAND ----------

df_Products.display()

# COMMAND ----------

# Extract content of the ProductSKU before the first -

df_Products = df_Products.withColumn('ProductSKU', split(col('ProductSKU'), ',')[0])

df_Products.display()


# COMMAND ----------

# Extract content of the ProductName before the first ' '

df_Products = df_Products.withColumn('ProductName', split(col('ProductName'), ' ')[0])

df_Products.display()

# COMMAND ----------

df_Products.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Products")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Frame Returns**

# COMMAND ----------

df_Returns.display()

# COMMAND ----------

df_Returns.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Returns")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Territories

# COMMAND ----------

df_Territories.display()

# COMMAND ----------

df_Returns.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_Territories")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Frame Sales Transformation

# COMMAND ----------

df_Sales.display()

# COMMAND ----------

df_Sales = df_Sales.withColumn('StockDate', to_timestamp(col('StockDate')))

df_Sales.display()

# COMMAND ----------

df_Sales = df_Sales.withColumn('OrderNumber', regexp_replace(col('OrderNumber'),'S','T'))

df_Sales.display()

# COMMAND ----------

# Multiplying the OrderLineItem with OrderQuantity resulting into another column

df_Sales = df_Sales.withColumn('Multiply', col('OrderLineItem') * col('OrderQuantity'))


df_Sales.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sales Analysis

# COMMAND ----------

df_Sales.display()

# COMMAND ----------

df_Sales.write.format('parquet')\
    .mode('append')\
    .option("path", "abfss://silver@datalakeengproject01bdv.dfs.core.windows.net/AdventureWorks_AdventureWorks_Sales")\
    .save()

# COMMAND ----------

df_Sales.groupBy('OrderDate').agg(count('OrderNumber').alias('total_order')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Product Categories

# COMMAND ----------

df_Product_Categories.display()