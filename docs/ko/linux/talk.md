---
layout: page
title: linux/talk (한국어)
description: "시각적 커뮤니케이션 프로그램으로, 사용자의 터미널에서 다른 사용자의 터미널로 라인을 복사합니다."
content_hash: 3bf8fd5a92482d7b53848239d79b129364bdd881
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/talk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/talk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# talk

시각적 커뮤니케이션 프로그램으로, 사용자의 터미널에서 다른 사용자의 터미널로 라인을 복사합니다.
더 많은 정보: <https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>.

- 동일한 기기에서 사용자의 talk 세션 시작:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 동일한 기기의 tty3에 로그인된 사용자와 talk 세션 시작:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty3</span>

- 원격 기기의 사용자와 talk 세션 시작:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 양쪽 터미널 화면의 텍스트 지우기:

`<Ctrl>+D`

- talk 세션 종료:

`<Ctrl>+C`
