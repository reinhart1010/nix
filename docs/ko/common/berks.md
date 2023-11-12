---
layout: page
title: common/berks (한국어)
description: "Chef 자세한 설명서 의존 관리자."
content_hash: f8639d110dcae038378089c4c802873edcc43d32
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/berks.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/berks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# berks

Chef 자세한 설명서 의존 관리자.
더 많은 정보: <https://docs.chef.io/berkshelf.html>.

- 로컬 저장소에 자세한 설명서 종속성 설치:

`berks install`

- 특정 자세한 설명서와 그 종속성을 업데이트:

`berks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자세한 설명서</span>

- 자세한 설명서를 Chef server에 업로드:

`berks upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자세한 설명서</span>

- 자세한 설명서의 종속성 확인:

`berks contingent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자세한 설명서</span>
