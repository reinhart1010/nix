---
layout: page
title: common/aws-glue (English)
description: "CLI for AWS Glue."
content_hash: 4d4b1b5e40058b00fdfbb3a0e3b98c2acbe91d14
---
# aws glue

CLI for AWS Glue.
Defines the public endpoint for the AWS Glue service.
More information: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- List jobs:

`aws glue list-jobs`

- Start a job:

`aws glue start-job-run --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>

- Start running a workflow:

`aws glue start-workflow-run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_name</span>

- List triggers:

`aws glue list-triggers`

- Start a trigger:

`aws glue start-trigger --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger_name</span>

- Create a dev endpoint:

`aws glue create-dev-endpoint --endpoint-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_arn_used_by_endpoint</span>
