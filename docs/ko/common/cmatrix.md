---
layout: page
title: common/cmatrix (한국어)
description: "터미널에 화면과 같이 스크롤링되는 Matrix를 표시."
content_hash: aca6d10e0d98baec53c4355b99adb6143ffb6175
last_modified_at: 2024-10-08
related_topics:
  - title: català version
    url: /ca/common/cmatrix.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cmatrix.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmatrix.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cmatrix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cmatrix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmatrix

터미널에 화면과 같이 스크롤링되는 Matrix를 표시.
더 많은 정보: <https://github.com/abishekvashok/cmatrix>.

- 비동기([a]synchronous) 스크롤 활성화:

`cmatrix -a`

- 텍스트 색상([C]olor) 변경 (기본적으로 녹색):

`cmatrix -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>

- [r]ainbow 모드 활성화:

`cmatrix -r`

- 100 센티초 (1초)의 화면 업데이트([u]pdate) 지연을 사용:

`cmatrix -u 100`
