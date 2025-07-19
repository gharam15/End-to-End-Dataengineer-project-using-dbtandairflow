#!/bin/bash

airflow db init
airflow users create \
  --username "$_AIRFLOW_WWW_USER_USERNAME" \
  --firstname "$_AIRFLOW_WWW_USER_FIRSTNAME" \
  --lastname "$_AIRFLOW_WWW_USER_LASTNAME" \
  --role Admin \
  --email "$_AIRFLOW_WWW_USER_EMAIL" \
  --password "$_AIRFLOW_WWW_USER_PASSWORD"

exec airflow webserver
