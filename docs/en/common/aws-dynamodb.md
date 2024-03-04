---
layout: page
title: common/aws-dynamodb (English)
description: "Manipulate an AWS Dynamodb database, a fast NoSQL database with predictable performance and seamless scalability."
content_hash: 19c49cbc0c05a5b9477b06aeafdca556c16ed7e9
last_modified_at: 2024-03-04
tldri18n_status: 2
---
# aws dynamodb

Manipulate an AWS Dynamodb database, a fast NoSQL database with predictable performance and seamless scalability.
More information: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- Create a table:

`aws dynamodb create-table --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --attribute-definitions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AttributeName=S,AttributeType=S</span>` --key-schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AttributeName=S,KeyType=HASH</span>` --provisioned-throughput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ReadCapacityUnits=5,WriteCapacityUnits=5</span>

- List all tables in the DynamoDB:

`aws dynamodb list-tables`

- Get details about a specific table:

`aws dynamodb describe-table --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>

- Add an item to a table:

`aws dynamodb put-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --item '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"AttributeName": {"S": "value"}</span>`}'`

- Retrieve an item from a table:

`aws dynamodb get-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}'`

- Update an item in the table:

`aws dynamodb update-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}' --update-expression "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SET Name = :n</span>`" --expression-attribute-values '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{":n": {"S": "Jane"}</span>`}'`

- Scan items in the table:

`aws dynamodb scan --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>

- Delete an item from the table:

`aws dynamodb delete-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}'`
