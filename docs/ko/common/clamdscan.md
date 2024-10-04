---
layout: page
title: common/clamdscan (한국어)
description: "ClamAV 데몬을 사용하여 바이러스를 검사."
content_hash: 3f3754781da68de2c0db4e438029eed9ce0f5f48
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clamdscan

ClamAV 데몬을 사용하여 바이러스를 검사.
더 많은 정보: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- 취약점이 있는지 파일이나 디렉터리를 스캔:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- `stdin`로부터 데이터를 스캔:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | clamdscan -`

- 현재 디렉터리를 검사하고 감염된 파일만 출력:

`clamdscan --infected`

- 스캔 보고서를 로그 파일로 인쇄:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그_파일</span>

- 감염된 파일을 특정 디렉토리로 이동:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/격리되는_디렉토리</span>

- 감염된 파일을 제거:

`clamdscan --remove`

- 여러 스레드를 사용하여 디렉터리를 검사:

`clamdscan --multiscan`

- 파일을 데몬으로 스트리밍하는 대신 파일 설명자를 전달:

`clamdscan --fdpass`
