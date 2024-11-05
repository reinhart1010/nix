---
layout: page
title: common/pnmtotiffcmyk (한국어)
description: "PNM 이미지를 CMYK로 인코딩된 TIFF로 변환."
content_hash: 8faebf8e4d9dca5df0ef3f46f90bcb9d152dc514
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmtotiffcmyk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtotiffcmyk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtotiffcmyk

PNM 이미지를 CMYK로 인코딩된 TIFF로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

- PNM 이미지를 CMYK로 인코딩된 TIFF로 변환:

`pnmtotiffcmyk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>

- TIFF 압축 방식 지정:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>

- 채우기 순서 제어:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">msb2lsb|lsb2msb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>
