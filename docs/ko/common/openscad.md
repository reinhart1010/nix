---
layout: page
title: common/openscad (한국어)
description: "솔리드 3D CAD 객체를 생성하는 소프트웨어."
content_hash: a530f799984b2f84f21fdefabd3bea2d5691efbc
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/openscad.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openscad.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openscad

솔리드 3D CAD 객체를 생성하는 소프트웨어.
더 많은 정보: <https://openscad.org>.

- 파일 열기:

`openscad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/button.scad</span>

- 파일을 STL로 변환:

`openscad -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/button.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/button.scad</span>

- 특정 색 구성표로 파일을 PNG로 렌더링:

`openscad -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/button.png</span>` --colorscheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Sunset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/button.scad</span>
