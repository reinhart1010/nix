---
layout: page
title: common/aws-batch (한국어)
description: "AWS Batch를 통해 배치 컴퓨팅 워크로드를 실행합니다."
content_hash: 6b97c0d859a8a01a13c20ce7b087dbb2b7ca1bcb
last_modified_at: 2023-10-01
related_topics:
  - title: English version
    url: /en/common/aws-batch.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws batch

AWS Batch를 통해 배치 컴퓨팅 워크로드를 실행합니다.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html>.

- 실행 중인 배치 작업 목록:

`aws batch list-jobs --job-queue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- 컴퓨팅 환경 생성:

`aws batch create-compute-environment --compute-environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compute_environment_name</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>

- 배치 작업 큐 생성:

`aws batch create-job-queue --job-queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` --compute-environment-order `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compute_environment</span>

- 작업 제출:

`aws batch submit-job --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --job-queue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_queue</span>` --job-definition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_definition</span>

- 배치 작업 목록 설명:

`aws batch describe-jobs --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jobs</span>

- 작업 취소:

`aws batch cancel-job --job-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --reason `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>
