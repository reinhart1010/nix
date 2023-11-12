---
layout: page
title: common/complete (한국어)
description: "쉘 명령어에 자동 완성 인자를 제공합니다."
content_hash: c9fc2ec357ccbf190c2d648b707870d33604dbb7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/complete.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/complete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# complete

쉘 명령어에 자동 완성 인자를 제공합니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- 함수에 명령어 자동 완성 기능을 적용합니다:

`complete -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 다른 명령어에 명령어 자동 완성 기능을 적용합니다:

`complete -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자동완성_명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 작성 완료된 단어에 공백을 추가하지 않고 자동 완성 기능을 적용합니다:

`complete -o nospace -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
