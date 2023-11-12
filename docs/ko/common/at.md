---
layout: page
title: common/at (한국어)
description: "명령 실행 후 한 번 실행합니다."
content_hash: ff5b1135be7334a4319f719b646a5523d2d3b22f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

명령 실행 후 한 번 실행합니다.
서비스 AD(또는 ATRUN)는 실제 실행을 위해 실행되어야 합니다.
더 많은 정보: <https://manned.org/at>.

- 표준 입력에서 명령을 5분 내에 실행(작업이 끝나면 `Ctrl + D` 를 누르세요):

`at now + 5 minutes`

- 오전 10시에 표준 입력에서 명령을 실행하십시오:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- 다음 주 화요일에 주어진 파일에서 명령을 실행하십시오:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>` 9:30 PM Tue`
