---
layout: page
title: linux/sm (한국어)
description: "전체 화면에 짧은 메시지를 표시합니다."
content_hash: ef785fabdba87cc804a7eb5023661780fbf04197
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sm

전체 화면에 짧은 메시지를 표시합니다.
더 많은 정보: <https://github.com/nomeata/screen-message>.

- 메시지를 전체 화면에 표시:

`sm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- 색상을 반전하여 메시지를 표시:

`sm -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- 사용자 지정 전경색으로 메시지를 표시:

`sm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파란색</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- 사용자 지정 배경색으로 메시지를 표시:

`sm -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#008888</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- 메시지를 3회 회전하여 표시 (90도씩 반시계 방향):

`sm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- 다른 명령의 출력을 사용하여 메시지를 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Hello World!"</span>` | sm -`
