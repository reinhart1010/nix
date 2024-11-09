---
layout: page
title: linux/duc (한국어)
description: "디스크 사용량을 색인화, 검사 및 시각화하는 도구 모음."
content_hash: 682eed11fa2bdb1c70ab0c811516613e90230a19
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/duc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

디스크 사용량을 색인화, 검사 및 시각화하는 도구 모음.
Duc는 파일 시스템의 폴더 누적 크기를 데이터베이스로 유지하여 이를 쿼리하거나 데이터의 위치를 나타내는 멋진 그래프를 생성할 수 있게 합니다.
더 많은 정보: <http://duc.zevv.nl>.

- `/usr` 폴더를 색인하고 기본 데이터베이스 위치 `~/.duc.db`에 기록:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- `/usr/local` 아래의 모든 파일과 폴더를 나열하고 상대적 파일 크기를 [g]그래프로 표시:

`duc ls --classify --graph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- `/usr/local` 아래의 모든 파일과 폴더를 트리뷰로 재귀적으로 나열:

`duc ls --classify --graph --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- 선버스트 그래프를 사용하여 파일 시스템을 탐색하는 그래픽 인터페이스 시작:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- 파일 시스템을 탐색하기 위한 ncurses 콘솔 인터페이스 실행:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- 데이터베이스 정보 덤프:

`duc info`
