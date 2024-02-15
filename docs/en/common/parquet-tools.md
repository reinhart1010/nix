---
layout: page
title: common/parquet-tools (English)
description: "Show, inspect and manipulate Parquet file."
content_hash: 6a4030838f8f0fe98f4de8255997567b797bcfa7
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# parquet-tools

Show, inspect and manipulate Parquet file.
More information: <https://github.com/apache/parquet-mr>.

- Display the content of a Parquet file:

`parquet-tools cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Display the first few lines of a Parquet file:

`parquet-tools head `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Print the schema of a Parquet file:

`parquet-tools schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Print the metadata of a Parquet file:

`parquet-tools meta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Print the content and metadata of a Parquet file:

`parquet-tools dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Concatenate several Parquet files into the target one:

`parquet-tools merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_parquet</span>

- Print the count of rows in a Parquet file:

`parquet-tools rowcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>

- Print the column and offset indexes of a Parquet file:

`parquet-tools column-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/parquet</span>
