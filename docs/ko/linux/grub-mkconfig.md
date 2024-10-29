---
layout: page
title: linux/grub-mkconfig (한국어)
description: "GRUB 구성 파일 생성."
content_hash: 616d3a7235e138ddeb6b4d2ca292df6134e7e578
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-mkconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grub-mkconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grub-mkconfig

GRUB 구성 파일 생성.
더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- 시뮬레이션을 실행하고 구성을 `stdout`에 출력:

`sudo grub-mkconfig`

- 구성 파일 생성:

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- 도움말 표시:

`grub-mkconfig --help`
