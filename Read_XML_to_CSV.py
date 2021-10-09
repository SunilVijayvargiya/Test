# Databricks notebook source
df = spark.read.text("dbfs:/mnt/NSAA/TextFile/RSSdatafeeder.xml")

# COMMAND ----------

df.display()

# COMMAND ----------

df = spark.read.format("xml").option("rowTag", "item").load("dbfs:/mnt/NSAA/TextFile/RSSdatafeeder.xml")

# COMMAND ----------

df.select("title","link","pubDate").write.mode("append").format("com.databricks.spark.csv").option("header","true").csv("dbfs:/mnt/NSAA/TextFile/XMLCSV")
