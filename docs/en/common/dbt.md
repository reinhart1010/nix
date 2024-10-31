---
layout: page
title: common/dbt (English)
description: "A tool to model transformations in data warehouses."
content_hash: 96ecd186eb5377ff9050c328ed2faa771d848538
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# dbt

A tool to model transformations in data warehouses.
More information: <https://github.com/dbt-labs/dbt-core>.

- Debug the dbt project and the connection to the database:

`dbt debug`

- Run all models of the project:

`dbt run`

- Run all tests of `example_model`:

`dbt test --select example_model`

- Build (load seeds, run models, snapshots, and tests associated with) `example_model` and its downstream dependents:

`dbt build --select example_model+`

- Build all models, except the ones with the tag `not_now`:

`dbt build --exclude "tag:not_now"`

- Build all models with tags `one` and `two`:

`dbt build --select "tag:one,tag:two"`

- Build all models with tags `one` or `two`:

`dbt build --select "tag:one tag:two"`
