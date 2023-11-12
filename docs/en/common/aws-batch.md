---
layout: page
title: common/aws-batch (English)
description: "Run batch computing workloads through the AWS Batch service."
content_hash: da787286d98343468b3f4977c69d7fef4f1d9eb6
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/aws-batch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws batch

Run batch computing workloads through the AWS Batch service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html>.

- List running batch jobs:

`aws batch list-jobs --job-queue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Create compute environment:

`aws batch create-compute-environment --compute-environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compute_environment_name</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>

- Create batch job queue:

`aws batch create-job-queue --job-queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` --compute-environment-order `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compute_environment</span>

- Submit job:

`aws batch submit-job --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --job-queue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_queue</span>` --job-definition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_definition</span>

- Describe the list of batch jobs:

`aws batch describe-jobs --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jobs</span>

- Cancel job:

`aws batch cancel-job --job-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --reason `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>
