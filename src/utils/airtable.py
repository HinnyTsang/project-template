""" 
    Airtable utils
    Hinny Tsang
    2023-03-06
"""
import os
import pandas as pd
import yaml

from dotenv import load_dotenv
from pyairtable import Table
from pyspark.sql import SparkSession, DataFrame

from src.logger.logger import logger


def read_airtable_as_pandas_dataframe(api_key: str, base_id: str, table_name: str) -> pd.DataFrame:
    """read_table 

    :param api_key: Your API key
    :type api_key: str
    :param base_id: Airtable base id
    :type base_id: str
    :param table_name: Airtable table name
    :type table_name: str
    :return: The fetched table
    :rtype: pd.DataFrame
    """
    table_name = Table(api_key, base_id, table_name)

    # Fetch all record from airtable
    table_data = table_name.all()

    # Convert to a list of dictionaries
    records = [record["fields"] for record in table_data]

    # Convert into pandas dataframe
    dataframe = pd.DataFrame(records)

    return dataframe


def read_airtable_as_pyspark_dataframe(spark: SparkSession,
                                       api_key: str,
                                       base_id: str,
                                       table_name: str) -> DataFrame:
    """read_table 

    :param api_key: _description_
    :type api_key: str
    :param base_id: _description_
    :type base_id: str
    :param table: _description_
    :type table: str
    :return: _description_
    :rtype: DataFrame
    """
    df_pandas = read_airtable_as_pandas_dataframe(api_key, base_id, table_name)

    df_spark = spark.createDataFrame(df_pandas)

    return df_spark


def main():
    """Test file to check rather the config is working"""
    load_dotenv()

    access_token = os.getenv("AIRTABLE_PERSONAL_ACCESS_TOKENS")
    with open("config/airtable.yaml", "r", encoding="utf-8") as config:
        config = yaml.safe_load(config)

    # Read example to pandas dataframe
    logger.info("Testing with pandas dataframe")
    iris_pandas = read_airtable_as_pandas_dataframe(
        access_token, config["base-id"], config["table.iris.name"])
    print(iris_pandas.head(10))

    # Read example to spark dataframe
    logger.info("Testing with pyspark dataframe")
    spark = SparkSession.builder.appName("airtable").getOrCreate()
    iris_spark = read_airtable_as_pyspark_dataframe(
        spark, access_token, config["base-id"], config["table.iris.name"])
    iris_spark.show(10)
    spark.stop()


if __name__ == "__main__":
    main()
