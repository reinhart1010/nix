---
layout: page
title: common/gifdiff (한국어)
description: "동일한 시각적 모양을 위해 두 개의 GIF를 비교."
content_hash: 7978484db15a83732da3d177411525162386439d
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gifdiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gifdiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gifdiff

동일한 시각적 모양을 위해 두 개의 GIF를 비교.
참고: `gifsicle`.
더 많은 정보: <https://www.lcdf.org/gifsicle>.

- GIF가 어떻게 다른지 확인:

`gifdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첫번째파일.gif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/두번째파일.gif</span>

- GIF가 다른지 확인:

`gifdiff --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첫번째파일.gif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/두번째파일.gif</span>
