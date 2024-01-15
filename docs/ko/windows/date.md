---
layout: page
title: windows/date (한국어)
description: "시스템 날짜 설정 또는 표시."
content_hash: 668818b287ff181983ab76ea9ee91efb4e0451d4
last_modified_at: 2024-01-15
related_topics:
  - title: বাংলা version
    url: /bn/windows/date.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/date.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/date.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/date.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># date

시스템 날짜 설정 또는 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/date>.

- 현재 시스템 날짜를 표시하고 새 날짜를 입력하라는 메시지를 표시(변경되지 않은 상태로 유지하려면 비워두기):

`date`

- 새 날짜를 묻는 메시지를 표시하지 않고 현재 시스템 날짜 표시:

`date /t`

- 현재 시스템 날짜를 특정 날짜로 변경:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>
