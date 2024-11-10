---
layout: page
title: linux/pkginfo (한국어)
description: "CRUX 시스템에서 패키지 데이터베이스를 조회."
content_hash: d4ed39243c6e28481538499b25bfcc06d1076f02
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pkginfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkginfo

CRUX 시스템에서 패키지 데이터베이스를 조회.
더 많은 정보: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- 설치된 패키지 및 버전 나열:

`pkginfo -i`

- 패키지가 소유한 파일 나열:

`pkginfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패턴과 일치하는 파일의 소유자(들) 나열:

`pkginfo -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 파일의 풋프린트 출력:

`pkginfo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
