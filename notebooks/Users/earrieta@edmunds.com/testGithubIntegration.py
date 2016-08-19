# Databricks notebook source exported at Fri, 19 Aug 2016 19:13:20 UTC
#naive fibonacci numbers
def fibonacci_numbers(number):
  if number <= 0:
    return 0
  elif number == 1:
    return number
  else:
    return fibonacci_numbers(number-1) + fibonacci_numbers(number-2)

# COMMAND ----------

fibonacci_numbers(2)