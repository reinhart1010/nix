---
layout: page
title: linux/gummy (한국어)
description: "Linux/X11용 화면 밝기/온도 관리 도구."
content_hash: 6dbf5635aac7f1a8d65e4b37d7062450729ca500
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gummy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gummy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gummy

Linux/X11용 화면 밝기/온도 관리 도구.
더 많은 정보: <https://github.com/Gitoffthelawn/gummy>.

- 화면 온도를 3000K로 설정:

`gummy --temperature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3000</span>

- 화면 백라이트를 50%로 설정:

`gummy --backlight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- 화면 픽셀 밝기를 45%로 설정:

`gummy --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">45</span>

- 현재 화면 픽셀 밝기를 10% 증가:

`gummy --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10</span>

- 현재 화면 픽셀 밝기를 10% 감소:

`gummy --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- 두 번째 화면의 온도와 픽셀 밝기를 설정:

`gummy --screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --temperature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3800</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">65</span>
