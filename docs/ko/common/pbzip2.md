---
layout: page
title: common/pbzip2 (한국어)
description: "`bzip2` 파일 압축기의 병렬 구현."
content_hash: 0c732cf47cf6d4a55dff2a4ba519b460a63652b8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pbzip2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbzip2

`bzip2` 파일 압축기의 병렬 구현.
같이 보기: `bzip2`, `tar`.
더 많은 정보: <https://manned.org/pbzip2>.

- 파일 압축:

`pbzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 프로세서 수를 사용하여 파일 압축:

`pbzip2 -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 [d]압축:

`pbzip2 --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일.bz2</span>

- 도움말 표시:

`pbzip2 -h`
