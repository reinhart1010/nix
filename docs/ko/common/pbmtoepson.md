---
layout: page
title: common/pbmtoepson (한국어)
description: "PBM 이미지를 Epson 프린터 그래픽으로 변환."
content_hash: b2e012f73831a80f80f23cbab87387646126b775
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtoepson.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtoepson.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtoepson

PBM 이미지를 Epson 프린터 그래픽으로 변환.
같이 보기: `pbmtoescp2`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoepson.html>.

- PBM 이미지를 Epson 프린터 그래픽으로 변환:

`pbmtoepson `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.epson</span>

- 출력의 프린터 프로토콜 지정:

`pbmtoepson -protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">escp9|escp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.epson</span>

- 출력의 가로 DPI 지정:

`pbmtoepson -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60|72|80|90|120|144|240</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.epson</span>
