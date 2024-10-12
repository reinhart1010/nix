---
layout: page
title: common/bind (한국어)
description: "bash 단축키 및 변수를 관리하기 위한 bash 내장."
content_hash: f097b2cf6d62bbba216efeea8e2463b0a5f835a7
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/bind.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bind

bash 단축키 및 변수를 관리하기 위한 bash 내장.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- 모든 바인딩된 명령어와 해당 단축키를 나열:

`bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|-P</span>

- 단축키에 대한 명령어를 쿼리:

`bind -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 키 바인딩:

`bind -x '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_시퀸스</span>`":`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`'`

- 사용자 정의 바인딩 나열:

`bind -X`

- 도움말 표시:

`help bind`
