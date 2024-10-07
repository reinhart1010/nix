---
layout: page
title: linux/systemd-cgls (한국어)
description: "선택된 Linux 제어 그룹 계층의 내용을 트리 형태로 보여줍니다."
content_hash: ea5a2c95d9cdd10e2ca77f031f5ed1ba75706908
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-cgls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-cgls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-cgls

선택된 Linux 제어 그룹 계층의 내용을 트리 형태로 보여줍니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>.

- 시스템의 전체 제어 그룹 계층 표시:

`systemd-cgls`

- 특정 리소스 컨트롤러의 제어 그룹 트리 표시:

`systemd-cgls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu|memory|io</span>

- 하나 이상의 systemd 유닛의 제어 그룹 계층 표시:

`systemd-cgls --unit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit1 unit2 ...</span>
