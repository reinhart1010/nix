---
layout: page
title: common/at (한국어)
description: "명령 실행 후 한 번 실행합니다."
content_hash: ee7b75ee9b2faf709825b15b87c74cbf3db897a5
last_modified_at: 2024-11-02
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
  - title: Nederlands version
    url: /nl/common/at.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># at

명령 실행 후 한 번 실행합니다.
결과는 사용자의 메일로 전송됨.
더 많은 정보: <https://manned.org/at>.

- `atd` 데몬 시작:

`systemctl start atd`

- 대화형으로 명령을 생성하고, 5분 안에 실행 (완료되면 `<Ctrl> + D` 누르기):

`at now + 5 minutes`

- 대화형으로 명령을 생성하고, 특정 시간에 실행:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- 오늘 오전 10시에 `stdin`에서 명령을 실행:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`" | at 1000`

- 다음주 화요일에 지정된 파일에서 명령을 실행:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 9:30 PM Tue`
