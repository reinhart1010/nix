---
layout: page
title: common/termdown (한국어)
description: "명령줄을 위한 카운트다운 타이머와 스톱워치."
content_hash: 5aa25cbc828f540b1307a09736f421e0493165d9
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/termdown.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/termdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# termdown

명령줄을 위한 카운트다운 타이머와 스톱워치.
더 많은 정보: <https://github.com/trehn/termdown>.

- 스톱워치 시작:

`termdown`

- 1분 30초 카운트다운 시작:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>

- 1분 30초 카운트다운을 시작하고 종료 시 터미널 깜빡이기:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>` --blink`

- 카운트다운 위에 제목 표시:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">흥미로운 제목</span>`"`

- 현재 시간 표시:

`termdown --time`
