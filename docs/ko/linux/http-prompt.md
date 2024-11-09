---
layout: page
title: linux/http-prompt (한국어)
description: "자동 완성 및 구문 강조 기능을 갖춘 대화형 명령줄 HTTP 클라이언트."
content_hash: ed7c212bb97cb3b9739c55c4e4ebb5a00aec33f4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/http-prompt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/http-prompt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># http-prompt

자동 완성 및 구문 강조 기능을 갖춘 대화형 명령줄 HTTP 클라이언트.
더 많은 정보: <https://github.com/httpie/http-prompt>.

- 기본 URL <http://localhost:8000> 또는 이전 세션을 대상으로 세션 시작:

`http-prompt`

- 지정된 URL로 세션 시작:

`http-prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 초기 옵션과 함께 세션 시작:

`http-prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:8000/api</span>` --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명:비밀번호</span>
