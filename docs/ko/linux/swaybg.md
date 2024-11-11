---
layout: page
title: linux/swaybg (한국어)
description: "Wayland 합성기용 배경화면 도구."
content_hash: 3df436bde9fe753461a479ce8f7e46dafc772e09
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/swaybg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swaybg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swaybg

Wayland 합성기용 배경화면 도구.
더 많은 정보: <https://github.com/swaywm/swaybg/blob/master/swaybg.1.scd>.

- 배경화면을 [i]이미지로 설정:

`swaybg --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 배경화면 [m]모드 설정:

`swaybg --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stretch|fit|fill|center|tile|solid_color</span>

- 배경화면을 고정된 [c]색상으로 설정:

`swaybg --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"#rrggbb"</span>
