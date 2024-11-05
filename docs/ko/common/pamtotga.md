---
layout: page
title: common/pamtotga (한국어)
description: "Netpbm 이미지를 TrueVision Targa 파일로 변환."
content_hash: f8cec1e79fd9e61dfdf0de9665e4ba63249ad828
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamtotga.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamtotga.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtotga.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtotga

Netpbm 이미지를 TrueVision Targa 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtotga.html>.

- Netpbm 이미지를 TrueVision Targa 파일로 변환:

`pamtotga `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.tga</span>

- 출력 이미지의 색상 맵 지정:

`pamtotga -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmap|cmap16|mono|rgb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.tga</span>

- 버전 표시:

`pamtotga -version`
