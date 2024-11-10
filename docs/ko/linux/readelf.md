---
layout: page
title: linux/readelf (한국어)
description: "ELF 파일에 대한 정보를 표시합니다."
content_hash: adb3ec6c74915f4dcbf631491d61da68ab275d6b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/readelf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/readelf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readelf

ELF 파일에 대한 정보를 표시합니다.
더 많은 정보: <https://manned.org/readelf.1>.

- ELF 파일의 모든 정보 표시:

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- ELF 파일에 포함된 모든 헤더 표시:

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- ELF 파일의 심볼 테이블 섹션에 있는 항목 표시(존재하는 경우):

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- ELF 헤더 정보 표시:

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- ELF 섹션 헤더 정보 표시:

`readelf --section-headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>
