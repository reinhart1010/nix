---
layout: page
title: common/rc (한국어)
description: "현대적이고 단순한 포트 리스너 및 리버스 셸."
content_hash: 6ba65d7ca51b69aa8f24199184967066ad75a407
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/rc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rc

현대적이고 단순한 포트 리스너 및 리버스 셸.
`nc`와 유사.
더 많은 정보: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- 특정 포트에서 리스닝 시작:

`rc -lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 리버스 셸 시작:

`rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">셸</span>
