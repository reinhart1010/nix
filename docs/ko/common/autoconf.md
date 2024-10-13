---
layout: page
title: common/autoconf (한국어)
description: "소프트웨어 소스 코드 패키지를 자동으로 구성하는 구성 스크립트 생성."
content_hash: b9f9f51b887fe1860fba349ebe6480d3580ff4e1
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/autoconf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoconf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoconf

소프트웨어 소스 코드 패키지를 자동으로 구성하는 구성 스크립트 생성.
더 많은 정보: <https://www.gnu.org/software/autoconf>.

- `configure.ac` (있는 경우) 또는 `configure.in` 에서 구성 스크립트를 생성하고 이 스크립트를 `configure`에 저장:

`autoconf`

- 지정된 템플릿에서 구성 스크립트를 생성; `stdout`으로 출력:

`autoconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿-파일</span>

- 지정된 템플릿에서 구성 스크립트를 생성하고(입력 파일이 변경되지 않은 경우에도) 출력을 파일에 작성:

`autoconf --force --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿-파일</span>
