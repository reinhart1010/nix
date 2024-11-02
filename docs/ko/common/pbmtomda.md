---
layout: page
title: common/pbmtomda (한국어)
description: "PBM 이미지를 Microdesign MDA 파일로 변환."
content_hash: ad4a2595a11c3f24d19ed5958bc58a3ddeac156d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtomda.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtomda.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtomda

PBM 이미지를 Microdesign MDA 파일로 변환.
같이 보기: `mdatopbm`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtomda.html>.

- PBM 이미지를 MDA 파일로 변환:

`pbmtomda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.mda</span>

- 입력 이미지의 색상을 반전:

`pbmtomda -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.mda</span>

- 입력 이미지의 높이를 절반으로 줄임:

`pbmtomda -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.mda</span>
