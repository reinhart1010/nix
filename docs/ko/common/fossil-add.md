---
layout: page
title: common/fossil-add (한국어)
description: "파일이나 디렉터리를 Fossil 버전 관리하에 두는 것."
content_hash: 80429b2572c6f2976ba5c82401026f7c0b49e866
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fossil-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fossil-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil add

파일이나 디렉터리를 Fossil 버전 관리하에 두는 것.
더 많은 정보: <https://fossil-scm.org/home/help/add>.

- 파일이나 디렉토리를 버전 관리하에 두어, 현재 체크아웃 상태가 되도록 함:

`fossil add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 현재 체크아웃에서 추가된 모든 파일을 제거:

`fossil add --reset`
