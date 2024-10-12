---
layout: page
title: common/gcloud-logging-logs-list (한국어)
description: "Google Cloud 프로젝트에서 로그 목록을 나열합니다."
content_hash: ef35510a4861218445e87a41b0073d50807707cb
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-logging-logs-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud logging logs list

Google Cloud 프로젝트에서 로그 목록을 나열합니다.
모니터링 및 분석을 위한 사용 가능한 로그 식별에 유용합니다. 같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/logging/logs/list>.

- 현재 프로젝트의 모든 로그 나열:

`gcloud logging logs list`

- 특정 로그 버킷 및 위치의 모든 로그 나열:

`gcloud logging logs list --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_아이디</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>

- 로그 버킷의 특정 뷰에 대한 모든 로그 나열:

`gcloud logging logs list --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_아이디</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>` --view=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">뷰_아이디</span>

- 필터 표현식을 사용하여 로그 나열:

`gcloud logging logs list --filter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>`"`

- 지정된 수의 로그 나열:

`gcloud logging logs list --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 특정 필드를 기준으로 오름차순 또는 내림차순(`~`는 내림차순)으로 정렬하여 로그 나열:

`gcloud logging logs list --sort-by="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>`"`

- 여러 필드를 기준으로 정렬하여 로그 나열:

`gcloud logging logs list --sort-by="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드1</span>`,~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드2</span>`"`

- 추가 세부 정보를 보여주는 자세한 출력으로 로그 나열:

`gcloud logging logs list --verbosity=debug`
