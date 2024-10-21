---
layout: page
title: common/giftopnm (한국어)
description: "GIF 파일을 PNM 이미지로 변환."
content_hash: d16c743b23a290002ce06b18c447440f55eb36ca
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/giftopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/giftopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># giftopnm

GIF 파일을 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/giftopnm.html>.

- GIF 이미지를 픽셀 단위의 Netpbm 이미지로 변환:

`giftopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pnm</span>

- 버전 정보 표시:

`giftopnm -version`
