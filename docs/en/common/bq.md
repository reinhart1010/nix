---
layout: page
title: common/bq (English)
description: "A Python-based tool for BigQuery, Google Cloud's fully managed and completely serverless enterprise data warehouse."
content_hash: d25e1630970ad9e88c1a6d77b9ae68d6cb97f53a
last_modified_at: 2024-04-19
tldri18n_status: 2
---
# bq

A Python-based tool for BigQuery, Google Cloud's fully managed and completely serverless enterprise data warehouse.
More information: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Run query against a BigQuery table using standard SQL, add `--dry_run` flag to estimate the number of bytes read by the query:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DATASET_NAME</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TABLE_NAME</span>`'`

- Run a parameterized query:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Create a new dataset or table in the US location:

`bq mk --location=US `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset_name</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>

- List all datasets in a project:

`bq ls --filter labels.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` --max_results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>` --format=prettyjson --project_id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id</span>

- Batch load data from a specific file in formats such as CSV, JSON, Parquet, and Avro to a table:

`bq load --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>` --source_format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CSV|JSON|PARQUET|AVRO</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path_to_source</span>

- Copy one table to another:

`bq cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OLD_TABLE</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_table</span>

- Display help:

`bq help`
