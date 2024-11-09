---
layout: page
title: common/sgitopnm (한국어)
description: "SGI 파일을 PNM 파일로 변환."
content_hash: 07f60787b9339b07c212c032cb5a00e111f92402
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sgitopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sgitopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sgitopnm

SGI 파일을 PNM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/sgitopnm.html>.

- SGI 이미지를 PNM 파일로 변환:

`sgitopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.sgi</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- SGI 파일에 대한 정보 표시:

`sgitopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.sgi</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- SGI 파일의 n 채널 추출:

`sgitopnm -channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.sgi</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
