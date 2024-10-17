---
layout: page
title: common/duc (한국어)
description: "디스크 사용량을 인덱싱, 검사, 시각화하기 위한 도구 모음."
content_hash: 70600f78369e9fc0b22e522f0c3707cf27164bd3
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/duc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/duc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

디스크 사용량을 인덱싱, 검사, 시각화하기 위한 도구 모음.
Duc는 파일 시스템 디렉토리의 누적 크기에 대한 데이터베이스를 유지 및 관리하여, 데이터베이스에서 쿼리를 허용하거나, 데이터 위치를 보여주는 멋있는 그래프를 생성.
더 많은 정보: <http://duc.zevv.nl>.

- /usr 디렉터리를 색인화하여, 기본 데이터베이스 위치 ~/.duc.db에 기록:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- /usr/local 아래의 모든 파일과 디렉터리를 나열, 그래프([g]raph)에 상대 파일 크기를 표시:

`duc ls -Fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- treeview를 반복적으로 사용해 /usr/local 아래의 모든 파일과 디렉터리를 나열:

`duc ls -Fg -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- sunburst 그래프를 사용하여 파일 시스템을 탐색하려면, 그래픽 인터페이스를 시작:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- ncurses 콘솔 인터페이스를 실행하여, 파일 시스템을 탐색:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- 데이터베이스 정보 덤프:

`duc info`
