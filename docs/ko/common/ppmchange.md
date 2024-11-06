---
layout: page
title: common/ppmchange (한국어)
description: "PPM 이미지에서 특정 색상의 모든 픽셀을 다른 색상으로 변경."
content_hash: 17deda28392ce4662bc51bfefa915c6a7954da37
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmchange.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmchange

PPM 이미지에서 특정 색상의 모든 픽셀을 다른 색상으로 변경.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmchange.html>.

- 각 `옛색상` - `새색상` 쌍에서 첫 번째 색상을 두 번째 색상으로 교체:

`ppmchange `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옛색상1 새색상1 옛색상2 새색상2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 동일하다고 간주되기 위한 색상의 유사도를 지정:

`ppmchange -closeness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">퍼센트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옛색상1 새색상1 옛색상2 새색상2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 인수에 지정되지 않은 모든 픽셀을 특정 색상으로 대체:

`ppmchange -remainder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옛색상1 새색상1 옛색상2 새색상2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
