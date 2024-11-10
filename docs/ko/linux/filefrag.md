---
layout: page
title: linux/filefrag (한국어)
description: "특정 파일의 단편화 정도를 보고."
content_hash: 2d392340a97e020a98650208f309c42dadf98de2
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/filefrag.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/filefrag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# filefrag

특정 파일의 단편화 정도를 보고.
더 많은 정보: <https://manned.org/filefrag>.

- 하나 이상의 [f]파일에 대한 보고서 표시:

`filefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 1024 바이트 블록 크기를 사용하여 보고서 표시:

`filefrag -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 블록 크기를 사용하여 보고서 표시:

`filefrag -b`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024|1K|1M|1G|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 매핑 요청 전 [f]파일 동기화:

`filefrag -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 확장 속성의 매핑 표시:

`filefrag -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 자세한 정보를 포함한 보고서 표시:

`filefrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
