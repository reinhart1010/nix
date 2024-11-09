---
layout: page
title: linux/nologin (한국어)
description: "사용자가 로그인하지 못하도록 하는 대체 셸."
content_hash: d8ba1a0b3fd65df04616ac46c8afbd249ee63936
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/nologin.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/nologin.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/nologin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nologin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nologin

사용자가 로그인하지 못하도록 하는 대체 셸.
더 많은 정보: <https://manned.org/nologin.5>.

- 사용자의 로그인 셸을 `nologin`으로 설정하여 로그인을 방지:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` nologin`

- `nologin` 로그인 셸을 가진 사용자에게 표시할 메시지 사용자 지정:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그인_거부_메시지</span>`" > /etc/nologin.txt`
