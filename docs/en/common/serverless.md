---
layout: page
title: common/serverless (English)
description: "Toolkit for deploying and operating serverless architectures on AWS, Google Cloud, Azure and IBM OpenWhisk."
content_hash: 7daf3e375a5570f0b5f94da8767afd955d4864f7
---
# serverless

Toolkit for deploying and operating serverless architectures on AWS, Google Cloud, Azure and IBM OpenWhisk.
Commands can be run either using the `serverless` command or its alias, `sls`.
More information: <https://serverless.com/>.

- Create a serverless project:

`serverless create`

- Create a serverless project from a template:

`serverless create --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_name</span>

- Deploy to a cloud provider:

`serverless deploy`

- Display information about a serverless project:

`serverless info`

- Invoke a deployed function:

`serverless invoke -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function_name</span>

- Follow the logs for a project:

`serverless logs -t`
