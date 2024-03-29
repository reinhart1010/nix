---
layout: page
title: common/boxes (한국어)
description: "ASCII 아트 상자 그리기, 제거 및 복구"
content_hash: 1c932c57ca1d125b5933ee50cbbf7df1481635df
last_modified_at: 2024-02-20
related_topics:
  - title: English version
    url: /en/common/boxes.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/boxes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># boxes

ASCII 아트 상자 그리기, 제거 및 복구
더 많은 정보: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- 문자열 주위에 상자 그리기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes`

- 문자열에서 상자를 제거:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -r`

- 문자열 주위에 특정 디자인의 상자 그리기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parchment</span>

- 너비가 10이고 높이가 5인 상자를 그리기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 중앙에 텍스트가 있는 상자 그리기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -a c`
