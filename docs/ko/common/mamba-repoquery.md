---
layout: page
title: common/mamba-repoquery (한국어)
description: "conda 및 mamba 패키지 저장소와 패키지 의존성을 효율적으로 조회."
content_hash: 1222b3ecf425c0fdf19fc3b4e01c2dd6b0d04e79
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mamba-repoquery.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mamba repoquery

conda 및 mamba 패키지 저장소와 패키지 의존성을 효율적으로 조회.
더 많은 정보: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- 특정 패키지의 사용 가능한 모든 버전 검색:

`mamba repoquery search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 제약 조건을 만족하는 모든 패키지 검색:

`mamba repoquery search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sphinx<5</span>

- 현재 활성화된 환경에 설치된 패키지의 의존성을 트리 형식으로 나열:

`mamba repoquery depends --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scipy</span>

- 특정 패키지의 설치가 필요한 현재 환경의 패키지를 출력 (`depends`의 역방향):

`mamba repoquery whoneeds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipython</span>
