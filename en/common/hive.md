---
layout: page
title: common/hive (English)
description: "CLI tool for Apache Hive."
content_hash: 266f874dd278aaa8dfd671363b147d31510815c8
---
# hive

CLI tool for Apache Hive.
More information: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>.

- Start a Hive interactive shell:

`hive`

- Run HiveQL:

`hive -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hiveql_query</span>`"`

- Run a HiveQL file with a variable substitution:

`hive --define `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Run a HiveQL with HiveConfig (e.g. `mapred.reduce.tasks=32`):

`hive --hiveconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conf_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conf_value</span>
