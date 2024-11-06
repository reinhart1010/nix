---
layout: page
title: common/xwdtopnm (한국어)
description: "X11 또는 X10 윈도우 덤프 파일을 PNM으로 변환."
content_hash: be34690092b36cd85e37fa072f8b425f122166d4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xwdtopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwdtopnm

X11 또는 X10 윈도우 덤프 파일을 PNM으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/xwdtopnm.html>.

- XWD 이미지 파일을 PBM으로 변환:

`xwdtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>

- 변환 과정에 대한 정보 표시:

`xwdtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>

- 입력 파일의 X11 헤더 내용 표시:

`xwdtopnm -headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>
