---
layout: page
title: common/odps (English)
description: "Aliyun ODPS (Open Data Processing Service) command-line tool."
content_hash: be39e337cddf6d044f928ea54194b5cdb272a63e
---
# odps

Aliyun ODPS (Open Data Processing Service) command-line tool.
Some subcommands such as `odps inst` have their own usage documentation.
More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Start the command-line with a custom configuration file:

`odpscmd --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">odps_config.ini</span>

- Switch current project:

`use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>`;`

- Show tables in the current project:

`show tables;`

- Describe a table:

`desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`;`

- Show table partitions:

`show partitions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`;`

- Describe a partition:

`desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` partition (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition_spec</span>`);`
