---
layout: page
title: common/gcloud-sql-export-sql (English)
description: "Export data from a Cloud SQL instance to a SQL file in Google Cloud Storage."
content_hash: 59e8bb5f75e11a75bbea1c89a701afd4169cdc52
last_modified_at: 2023-12-08
tldri18n_status: 2
---
# gcloud sql export sql

Export data from a Cloud SQL instance to a SQL file in Google Cloud Storage.
Useful for creating backups or migrating data. See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>.

- Export data from a specific Cloud SQL instance to a Google Cloud Storage bucket as a SQL dump file:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>

- Export data asynchronously, returning immediately without waiting for the operation to complete:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>` --async`

- Export data from specific databases within the Cloud SQL instance:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>` --database=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database1,database2,...</span>

- Export specific tables from a specified database within the Cloud SQL instance:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>` --database=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>` --table=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table1,table2,...</span>

- Export data while offloading the operation to a temporary instance to reduce strain on the source instance:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>` --offload`

- Export data and compress the output with `gzip`:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>`.gz`
