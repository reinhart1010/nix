---
layout: page
title: common/parquet-tools (English)
description: "A tool to show, inspect and manipulate Parquet file."
content_hash: 99e957987f95b0f31955ab569dfc60435f187159
---
# parquet-tools

A tool to show, inspect and manipulate Parquet file.
More information: <https://github.com/apache/parquet-mr/tree/master/parquet-tools-deprecated>.

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
