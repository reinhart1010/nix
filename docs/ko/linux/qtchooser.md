---
layout: page
title: linux/qtchooser (한국어)
description: "Qt 개발 바이너리 버전 간 선택을 돕는 래퍼."
content_hash: 5066c16456777add5783dfbab3c95ca823652a9e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/qtchooser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qtchooser

Qt 개발 바이너리 버전 간 선택을 돕는 래퍼.
더 많은 정보: <https://manned.org/qtchooser>.

- 구성 파일에서 사용 가능한 Qt 버전 나열:

`qtchooser --list-versions`

- 환경 정보 출력:

`qtchooser --print-env`

- 지정된 Qt 버전을 사용하여 지정된 도구 실행:

`qtchooser --run-tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도구</span>` --qt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전_이름</span>

- 선택할 수 있도록 Qt 버전 항목 추가:

`qtchooser --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/qmake</span>

- 도움말 표시:

`qtchooser --help`
