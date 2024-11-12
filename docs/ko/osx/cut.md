---
layout: page
title: osx/cut (한국어)
description: "`stdin` 또는 파일에서 필드를 잘라냅니다."
content_hash: 446d266deebd1d41a1db50502caee4babad15a0f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

`stdin` 또는 파일에서 필드를 잘라냅니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- 각 줄의 특정 문자/필드 범위 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- 특정 구분자로 각 줄의 필드 범위 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 특정 파일의 각 줄에서 문자 범위 출력:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
