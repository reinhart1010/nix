---
layout: page
title: linux/ifstat (한국어)
description: "네트워크 인터페이스 통계 보기."
content_hash: 931225c416a3767e98c3dc9c3fac7a259daeaa35
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ifstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ifstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifstat

네트워크 인터페이스 통계 보기.
더 많은 정보: <https://manned.org/ifstat>.

- 마지막 쿼리 이후의 네트워크 인터페이스 통계 보기:

`ifstat`

- 마지막 부팅 이후의 네트워크 인터페이스 통계 보기:

`ifstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ignore</span>

- 오류율 보기:

`ifstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--errors</span>
