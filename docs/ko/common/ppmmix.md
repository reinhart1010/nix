---
layout: page
title: common/ppmmix (한국어)
description: "두 개의 PPM 이미지를 혼합."
content_hash: e42c547824d32f4a43a05a5701c1403d1150eb6c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmmix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmmix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmmix

두 개의 PPM 이미지를 혼합.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmmix.html>.

- `fadefactor`를 사용하여 각 이미지의 가중치를 조절하여 지정된 PPM 이미지를 혼합:

`ppmmix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fadefactor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일1.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일2.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
