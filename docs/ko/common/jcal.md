---
layout: page
title: common/jcal (한국어)
description: "Jalali 형식으로 달력을 표시하며, 현재 날짜를 강조 표시."
content_hash: 8486f7f744e8282e8b7fb4921b5994ab7fc6e9df
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jcal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jcal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jcal

Jalali 형식으로 달력을 표시하며, 현재 날짜를 강조 표시.
더 많은 정보: <https://www.nongnu.org/jcal/>.

- 현재 월의 달력 표시:

`jcal`

- 이전, 현재 및 다음 달의 달력 표시:

`jcal -3`

- 특정 연도의 달력 표시 (4자리):

`jcal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 특정 월과 연도의 달력 표시:

`jcal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>
