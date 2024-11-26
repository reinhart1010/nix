---
layout: page
title: common/boxes (한국어)
description: "ASCII 아트 상자 그리기, 제거 및 복구"
content_hash: eef5eb90223d31db60d30164402e2f49e28f0a07
last_modified_at: 2024-11-26
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

- 문자열에서 상자를 제거[r]:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -r`

- 문자열 주위에 특정 디자인[d]의 상자 그리기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parchment</span>

- 상자 크기[s] 지정(열 단위):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 상자 텍스트 수평[h] 정렬[a](왼쪽[l], 중앙[c], 오른쪽[r]):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -a h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">l|c|r</span>

- 상자 텍스트 수직[v] 정렬[a](위쪽[t], 중앙[c], 아래쪽[b]):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -a v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t|c|b</span>

- 상자 텍스트 양쪽 조정[j](왼쪽[l], 중앙[c], 오른쪽[r]):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" | boxes -a j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">l|c|r</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vt</span>
