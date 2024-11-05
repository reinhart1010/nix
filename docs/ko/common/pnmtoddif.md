---
layout: page
title: common/pnmtoddif (한국어)
description: "PNM 이미지를 DDIF 이미지 파일로 변환."
content_hash: 19ba85f5113e2a45bc3c39d32356f36fa733addd
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmtoddif.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtoddif.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtoddif

PNM 이미지를 DDIF 이미지 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtoddif.html>.

- PNM 이미지를 DDIF 이미지 파일로 변환:

`pnmtoddif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ddif</span>

- 출력 이미지의 가로 및 세로 해상도를 명시적으로 지정:

`pnmtoddif -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수평_dpi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수직_dpi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ddif</span>
