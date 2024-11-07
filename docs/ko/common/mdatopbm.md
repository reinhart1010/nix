---
layout: page
title: common/mdatopbm (한국어)
description: "Microdesign MDA 파일을 PBM 이미지로 변환."
content_hash: 11af99d13af01220f2a1589cd46bff1cebfe16e5
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mdatopbm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mdatopbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mdatopbm

Microdesign MDA 파일을 PBM 이미지로 변환.
같이 보기: `pbmtomda`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/mdatopbm.html>.

- MDA 파일을 PBM 이미지로 변환:

`mdatopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 입력 이미지의 색상을 반전:

`mdatopbm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 입력 이미지의 높이를 두 배로:

`mdatopbm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
