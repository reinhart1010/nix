---
layout: page
title: common/aws-glue (한국어)
description: "AWS Glue용 CLI."
content_hash: 8c8ea1f633f8d6ff17bce7f9a96f753ed40572f9
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-glue.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-glue.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-glue.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-glue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws glue

AWS Glue용 CLI.
AWS Glue 서비스에 대한 퍼블릭 엔드포인트 정의.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- 작업 나열:

`aws glue list-jobs`

- 작업 시작:

`aws glue start-job-run --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 워크플로우 실행 시작:

`aws glue start-workflow-run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">워크플로우_이름</span>

- 트리거 나열:

`aws glue list-triggers`

- 트리거 시작:

`aws glue start-trigger --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트리거_이름</span>

- 개발 엔드포인트 생성:

`aws glue create-dev-endpoint --endpoint-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_arn_used_by_endpoint</span>
