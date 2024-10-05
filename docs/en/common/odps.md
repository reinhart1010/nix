---
layout: page
title: common/odps (English)
description: "Aliyun ODPS (Open Data Processing Service) command-line tool."
content_hash: c5ad8e9254a8cdf06d0bb8c6aaf18bbb3ddf787b
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# odps

Aliyun ODPS (Open Data Processing Service) command-line tool.
Some subcommands such as `inst` have their own usage documentation.
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
