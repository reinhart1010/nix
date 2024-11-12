---
layout: page
title: osx/opensnoop (한국어)
description: "시스템에서 파일 열림을 추적합니다."
content_hash: f2010e1b10c614b58a2288fdf6e7d67e7462a3a9
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/opensnoop.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/opensnoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/opensnoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opensnoop

시스템에서 파일 열림을 추적합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- 파일이 열릴 때마다 모두 출력:

`sudo opensnoop`

- 프로세스 이름으로 파일 열림 추적:

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`"`

- PID로 파일 열림 추적:

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 특정 파일을 여는 프로세스 추적:

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
