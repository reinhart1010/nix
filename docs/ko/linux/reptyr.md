---
layout: page
title: linux/reptyr (한국어)
description: "실행 중인 프로세스를 새로운 터미널로 이동."
content_hash: 71a3beb808262f4666e3475ac5eba68cee834fe7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/reptyr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/reptyr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reptyr

실행 중인 프로세스를 새로운 터미널로 이동.
`screen`에서 오래 실행되는 작업을 시작하는 것을 잊었을 때 가장 유용.
더 많은 정보: <https://github.com/nelhage/reptyr>.

- 실행 중인 프로세스를 현재 터미널로 이동:

`reptyr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>
