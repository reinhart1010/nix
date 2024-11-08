---
layout: page
title: linux/balooctl (한국어)
description: "KDE Plasma의 파일 색인 및 검색 프레임워크."
content_hash: 98ee96fc8a93783dd894dd593e45c321d99dd600
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/balooctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/balooctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/balooctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># balooctl

KDE Plasma의 파일 색인 및 검색 프레임워크.
더 많은 정보: <https://wiki.archlinux.org/index.php/Baloo>.

- 색인기의 상태 표시:

`balooctl status`

- 파일 색인기 활성화/비활성화:

`balooctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- 색인 데이터베이스 정리:

`balooctl purge`

- 파일 색인기 일시 중지:

`balooctl suspend`

- 파일 색인기 재개:

`balooctl resume`

- Baloo가 사용하는 디스크 공간 표시:

`balooctl indexSize`

- 색인되지 않은 파일이 있는지 확인하고 색인:

`balooctl check`

- 도움말 표시:

`balooctl --help`
