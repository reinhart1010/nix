---
layout: page
title: linux/oomctl (한국어)
description: "`systemd-oomd`에 저장된 상태를 분석합니다."
content_hash: 4971b5d6353e25f69a55acdc671b50c0c1e760a9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/oomctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/oomctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/oomctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/oomctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># oomctl

`systemd-oomd`에 저장된 상태를 분석합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/oomctl.html>.

- `systemd-oomd`에 의해 저장된 cgroups 및 시스템 컨텍스트의 현재 상태를 표시:

`oomctl dump`
