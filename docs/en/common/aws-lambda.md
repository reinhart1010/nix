---
layout: page
title: common/aws-lambda (English)
description: "CLI for AWS lambda."
content_hash: a11162c4553dd0816ca7b51355c0d3948c794c29
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/aws-lambda.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lambda

CLI for AWS lambda.
More information: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Run a function:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/response.json</span>

- Run a function with an input payload in JSON format:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/response.json</span>

- List functions:

`aws lambda list-functions`

- Display the configuration of a function:

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List function aliases:

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display the reserved concurrency configuration for a function:

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List which AWS services can invoke the function:

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
