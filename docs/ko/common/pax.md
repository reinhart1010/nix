---
layout: page
title: common/pax (한국어)
description: "아카이빙 및 복사 유틸리티."
content_hash: 4637d4b657bbbc488441fbe3a9d9f52a59faa0c8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pax.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pax

아카이빙 및 복사 유틸리티.
더 많은 정보: <https://manned.org/pax.1p>.

- 아카이브 내용 나열:

`pax -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar</span>

- `gzip` 아카이브 내용 나열:

`pax -zf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>

- 파일로부터 아카이브 생성:

`pax -wf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 출력 리디렉션을 사용해 파일로부터 아카이브 생성:

`pax -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟.tar</span>

- 현재 디렉토리에 아카이브 추출:

`pax -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tar</span>

- 원본 메타데이터를 유지하면서 디렉토리에 복사; `target/`은 존재해야 함:

`pax -rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target/</span>
