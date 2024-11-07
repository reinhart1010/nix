---
layout: page
title: common/dvc-checkout (한국어)
description: "캐시에서 데이터 파일 및 디렉토리를 체크아웃."
content_hash: ae49c294ce996b4d584c805f8dc5ba74e69df3c5
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-checkout.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dvc-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc checkout

캐시에서 데이터 파일 및 디렉토리를 체크아웃.
더 많은 정보: <https://dvc.org/doc/command-reference/checkout>.

- 모든 대상 파일 및 디렉토리의 최신 버전 체크아웃:

`dvc checkout`

- 지정된 대상의 최신 버전 체크아웃:

`dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 다른 Git 커밋/태그/브랜치에서 특정 버전의 대상 체크아웃:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시|태그|브랜치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` && dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>
