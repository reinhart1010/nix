---
layout: page
title: osx/rargs (한국어)
description: "각 표준 입력 줄에 대해 명령을 실행합니다."
content_hash: 7597834359458f85e3f77d36dd871bfc2fc6ca1a
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/rargs.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/rargs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rargs

각 표준 입력 줄에 대해 명령을 실행합니다.
패턴 매칭 지원이 있는 `xargs`와 유사합니다.
더 많은 정보: <https://github.com/lotabout/rargs>.

- 입력의 각 줄에 대해 명령을 실행 (`{0}`은 텍스트에 대체할 위치를 나타냄):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | rargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` {0}`

- 실제로 실행하지 않고 실행할 명령을 출력하는 드라이 런 수행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | rargs -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` {0}`

- 목록의 모든 파일에서 `.bak` [x]확장자 제거:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | rargs -p '(.*).bak mv {0} {1}`

- 병렬로 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | rargs -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_프로세스_수</span>

- 입력의 각 줄이 줄바꿈(`\n`) 대신 NUL 문자(`\0`)로 구분된 것으로 간주:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | rargs -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` {0}`
