---
layout: page
title: common/aws-kendra (English)
description: "CLI for AWS Kendra."
content_hash: fca95f0e0b8e9c31b6523ff9b166e085abf31130
last_modified_at: 2024-07-30
tldri18n_status: 2
---
# aws kendra

CLI for AWS Kendra.
More information: <https://docs.aws.amazon.com/cli/latest/reference/kendra/index.html>.

- Create an index:

`aws kendra create-index --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role-arn</span>

- List indexes:

`aws kendra list-indexes`

- Describe an index:

`aws kendra describe-index --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index-id</span>

- List data sources:

`aws kendra list-data-sources`

- Describe a data source:

`aws kendra describe-data-source --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data-source-id</span>

- List search queries:

`aws kendra list-query-suggestions --index-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index-id</span>` --query-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query-text</span>
