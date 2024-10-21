---
layout: page
title: common/fin (한국어)
description: "Docksal 명령줄 유틸리티."
content_hash: bd2e71cec44d7c719258aa2b9047217d1d1a6ff3
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fin

Docksal 명령줄 유틸리티.
더 많은 정보: <https://docs.docksal.io/fin/fin/>.

- 현재 디렉터리에서 프로젝트를 시작:

`fin project start`

- 현재 디렉터리에서 프로젝트를 중지:

`fin project stop`

- 특정 컨테이너에 쉘을 열기:

`fin bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 특정 컨테이너의 로그 표시:

`fin logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 특정 컨테이너의 로그 표시하고 로그를 계속 출력:

`fin logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>
