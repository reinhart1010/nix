---
layout: page
title: common/gcloud-components-install (한국어)
description: "Google Cloud CLI의 구성 요소와 그 의존성을 설치."
content_hash: aaacc4c035fa4e382ddf609d037c713828c71e75
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-components-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud components install

Google Cloud CLI의 구성 요소와 그 의존성을 설치.
기존 설치를 업그레이드하지 않고 현재 Google Cloud CLI 버전의 구성 요소를 설치.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/components/install>.

- 설치 가능한 구성 요소 보기:

`gcloud components list`

- 하나 이상의 구성 요소 설치 (필요한 의존성도 함께 설치):

`gcloud components install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_id1 구성_요소_id2 ...</span>

- 현재 Google Cloud CLI 버전 확인:

`gcloud version`

- Google Cloud CLI를 최신 버전으로 업데이트:

`gcloud components update`
