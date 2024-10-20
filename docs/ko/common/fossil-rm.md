---
layout: page
title: common/fossil-rm (한국어)
description: "Fossil 버전 관리에서 파일이나 디렉터리를 제거."
content_hash: 7ea05487462132a0eccaa4d826e3e30194c0ae2e
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fossil-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fossil-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil rm

Fossil 버전 관리에서 파일이나 디렉터리를 제거.
참고: `fossil forget`.
더 많은 정보: <https://fossil-scm.org/home/help/rm>.

- Fossil 버전 관리에서 파일이나 디렉터리를 제거:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- Fossil 버전 관리에서 파일이나 디렉터리를 제거하고, 디스크에서도 삭제:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- 이전에 제거하고 커밋하지 않은 모든 파일을 Fossil 버전 관리에 다시 추가:

`fossil rm --reset`
