---
layout: page
title: common/pnmtosgi (한국어)
description: "PNM 파일을 SGI 이미지 파일로 변환."
content_hash: 3f4f440b3a6ddf4038a61ab0204cf33fafc3f671
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmtosgi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtosgi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtosgi

PNM 파일을 SGI 이미지 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- PNM 이미지를 SGI 이미지로 변환:

`pnmtosgi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>

- 압축을 비활성화하거나 활성화:

`pnmtosgi -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verbatim|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>

- SGI 이미지 헤더의 `imagename` 필드에 지정된 문자열을 기록:

`pnmtosgi -imagename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>
