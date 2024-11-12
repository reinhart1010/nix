---
layout: page
title: linux/slapt-get (한국어)
description: "Slackware 패키지 관리를 위한 `apt`와 유사한 시스템."
content_hash: fce97c0c7fbcfbe5801fbd5cddcdcb3f4e069f28
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/slapt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slapt-get

Slackware 패키지 관리를 위한 `apt`와 유사한 시스템.
slapt-getrc 파일에서 패키지 소스를 구성해야 합니다.
더 많은 정보: <https://software.jaos.org>.

- 사용 가능한 패키지 및 버전 목록 업데이트:

`slapt-get --update`

- 패키지를 설치하거나 최신 버전으로 업데이트:

`slapt-get --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`slapt-get --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`slapt-get --upgrade`

- 패키지 이름, 디스크 세트 또는 버전으로 패키지 검색:

`slapt-get --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- 패키지에 대한 정보 표시:

`slapt-get --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
