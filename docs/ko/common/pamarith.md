---
layout: page
title: common/pamarith (한국어)
description: "두 개의 Netpbm 이미지에 이진 함수를 적용."
content_hash: c4b203c84fa0dac612202ec4b2101c42d3bb49b4
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamarith.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamarith.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamarith.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamarith

두 개의 Netpbm 이미지에 이진 함수를 적용.
같이 보기: `pamfunc`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamarith.html>.

- 지정된 이진 함수를 두 이미지에 대해 픽셀 단위로 적용 (이미지는 반드시 동일한 크기여야 함):

`pamarith -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|subtract|multiply|divide|difference|minimum|maximum|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.pam|pbm|pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.pam|pbm|pgm|ppm</span>
