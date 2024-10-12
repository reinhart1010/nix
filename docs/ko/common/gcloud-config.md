---
layout: page
title: common/gcloud-config (한국어)
description: "`gcloud`의 다양한 구성 관리."
content_hash: ee886a48baaabf89cce18dc5cc783735687df626
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud config

`gcloud`의 다양한 구성 관리.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/config>.

- 현재 구성에 대한 속성(예: compute/zone) 정의:

`gcloud config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- `gcloud` 속성의 값 가져오기:

`gcloud config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>

- 현재 구성의 모든 속성 표시:

`gcloud config list`

- 주어진 이름으로 새 구성 만들기:

`gcloud config configurations create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>

- 사용 가능한 모든 구성 목록 표시:

`gcloud config configurations list`

- 주어진 이름의 기존 구성으로 전환:

`gcloud config configurations activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>
