---
layout: page
title: linux/diffimg (한국어)
description: "두 이미지 간의 교차점을 계산합니다."
content_hash: ffe4dcc5d89702c3bf4a7a410c51a148580e7b91
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/diffimg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/diffimg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># diffimg

두 이미지 간의 교차점을 계산합니다.
참고: 지원되는 확장자는 `.png`, `.gif`, `.jpg`, `.ps`입니다.
더 많은 정보: <https://manned.org/diffimg>.

- 입력 이미지 간의 교차점을 계산하고, 각 픽셀이 입력 이미지의 해당 픽셀 간 차이를 나타내는 이미지를 출력:

`diffimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지1.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지2.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.ext</span>
