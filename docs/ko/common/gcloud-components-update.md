---
layout: page
title: common/gcloud-components-update (한국어)
description: "설치된 Google Cloud CLI 구성 요소를 최신 버전으로 업데이트."
content_hash: 19476365949622635a551c7a2d5a20db67af6f08
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-components-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud components update

설치된 Google Cloud CLI 구성 요소를 최신 버전으로 업데이트.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/components/update>.

- 모든 구성 요소를 최신 버전으로 업데이트:

`gcloud components update`

- 모든 구성 요소를 특정 버전으로 업데이트:

`gcloud components update --version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>

- 확인 없이 구성 요소 업데이트 (자동화 스크립트에 유용):

`gcloud components update --quiet`
