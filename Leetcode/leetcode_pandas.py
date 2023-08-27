"""Leetcode Pandas"""
import pandas as pd


# https://leetcode.com/JHarrisJoshua/


# ----------------- 183. Customers Who Never Order --------------------------  #
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    df.rename(columns={'name': 'Customers'}, inplace=True)
    return df[['Customers']]


# ------------------------ 595. Big Countries -------------------------------  #
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]


# ------------------------ 1148. Article Views I ---------------------------  #
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df.rename(columns={'author_id':'id'}, inplace=True)
    df.drop_duplicates(subset=['id'], inplace=True)
    df.sort_values(by=['id'], inplace=True)
    return df[['id']]


# --------------- 1757. Recyclable and Low Fat Products ---------------------  #
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return df[['product_id']]
