---
layout: page
title: common/histexpand (한국어)
description: "`sh`, Bash, Zsh, `rbash` 및 `ksh`에서 셸 기록을 재사용하고 확장."
content_hash: 1fd31ea0a02f2412cabaeaa7d9ba161e61c654a2
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/histexpand.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/histexpand.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/histexpand.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/histexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history expansion

`sh`, Bash, Zsh, `rbash` 및 `ksh`에서 셸 기록을 재사용하고 확장.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- 루트로 이전 명령을 실행 (`!!`는 이전 명령으로 대체됨):

`sudo !!`

- 이전 명령의 마지막 인수를 사용하여 명령을 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` !$`

- 이전 명령의 첫번째 인수를 사용하여 명령을 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` !^`

- history의 N번째 명령을 실행:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- history에서 `n`라인 명령을 다시 실행:

`!-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- `문자열`이 포함된 가장 최근 명령을 실행:

`!?`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`?`

- `문자열1`을 `문자열2`로 바꿔, 이전 명령을 실행:

`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1</span>`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열2</span>`^`

- history 확장을 수행하지만, 실제로 실행하는 대신 실행될 명령을 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
