---
layout: page
title: linux/reportbug (한국어)
description: "Debian 배포판의 버그 보고 도구."
content_hash: 602235cfc907639d9ce2498133f3af397b8d58f7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/reportbug.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/reportbug.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reportbug

Debian 배포판의 버그 보고 도구.
더 많은 정보: <https://manned.org/reportbug>.

- 특정 패키지에 대한 버그 보고서를 작성하고 이메일로 전송:

`reportbug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지와 관련 없는 버그(일반 문제, 인프라 등) 보고:

`reportbug other`

- 버그 보고서를 이메일로 보내지 않고 파일에 작성:

`reportbug -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
