---
layout: page
title: common/tlmgr-platform (한국어)
description: "TeX Live 플랫폼 관리."
content_hash: 0ef3e2787fceb2ce5c58506619ef356db5ecae42
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tlmgr-platform.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-platform.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr platform

TeX Live 플랫폼 관리.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 패키지 저장소에서 사용 가능한 모든 플랫폼 나열:

`tlmgr platform list`

- 특정 플랫폼에 대한 실행 파일 추가:

`sudo tlmgr platform add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>

- 특정 플랫폼에 대한 실행 파일 제거:

`sudo tlmgr platform remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>

- 현재 플랫폼을 자동으로 감지하여 전환:

`sudo tlmgr platform set auto`

- 특정 플랫폼으로 전환:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>
