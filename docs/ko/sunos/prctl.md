---
layout: page
title: sunos/prctl (한국어)
description: "실행 중인 프로세스, 작업 및 프로젝트의 리소스 제어를 가져오거나 설정합니다."
content_hash: f4f5eb6b5a0b4a19d4f7aa76d266dcfe50af42fd
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

실행 중인 프로세스, 작업 및 프로젝트의 리소스 제어를 가져오거나 설정합니다.
더 많은 정보: <https://www.unix.com/man-page/sunos/1/prctl>.

- 프로세스 제한 및 권한 검사:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 기계적 분석이 가능한 형식으로 프로세스 제한 및 권한 검사:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 실행 중인 프로세스의 특정 제한 가져오기:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
