---
layout: page
title: common/pnmhistmap (한국어)
description: "PNM 이미지의 히스토그램 그리기."
content_hash: feaa6d007dc82c6d85618a0da52e0d59acdc7724
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmhistmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmhistmap

PNM 이미지의 히스토그램 그리기.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

- PNM 이미지의 히스토그램 그리기:

`pnmhistmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 막대 대신 점으로 히스토그램 그리기:

`pnmhistmap -dots `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 포함할 강도 값의 범위 지정:

`pnmhistmap -lval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소값</span>` -rval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
