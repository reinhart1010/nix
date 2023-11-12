---
layout: page
title: common/bzip2 (한국어)
description: "블록 정렬 파일 압축기."
content_hash: b4c6d85c664f12d33a8ef22d8e3f5e7056d0d9ae
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bzip2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bzip2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bzip2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzip2

블록 정렬 파일 압축기.
더 많은 정보: <https://manned.org/bzip2>.

- 파일 압축하기:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축할_파일</span>

- 파일 압축해제하기:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz2</span>

- 파일을 표준 출력으로 압축해제:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz2</span>

- 압축된 파일 내 각 파일의 무결성 테스트:

`bzip2 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz2</span>

- 압축된 파일의 각 파일에 대한 압축률과 자세한 정보 표시:

`bzip2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz2</span>

- 기존 파일을 덮어쓰면서 파일 압축 해제:

`bzip2 --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz2</span>

- 도움말 표시:

`bzip2 -h`
