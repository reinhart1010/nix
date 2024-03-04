---
layout: page
title: common/aws-lambda (English)
description: "Use AWS Lambda, a compute service for running code without provisioning or managing servers."
content_hash: c0ae16c56252735e6e3bbcc50f6cb427c29e4867
last_modified_at: 2024-03-04
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

Use AWS Lambda, a compute service for running code without provisioning or managing servers.
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
