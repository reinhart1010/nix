---
layout: page
title: common/pnmtosgi (한국어)
description: "PNM 파일을 SGI 이미지 파일로 변환."
content_hash: 3f4f440b3a6ddf4038a61ab0204cf33fafc3f671
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtosgi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtosgi

PNM 파일을 SGI 이미지 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- PNM 이미지를 SGI 이미지로 변환:

`pnmtosgi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>

- 압축을 비활성화하거나 활성화:

`pnmtosgi -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verbatim|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>

- SGI 이미지 헤더의 `imagename` 필드에 지정된 문자열을 기록:

`pnmtosgi -imagename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sgi</span>
