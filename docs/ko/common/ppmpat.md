---
layout: page
title: common/ppmpat (한국어)
description: "패턴을 사용하여 PPM 이미지를 생성."
content_hash: 51754d39b9194ab8f6d8cf2976895ed2ca9a294a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmpat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmpat

패턴을 사용하여 PPM 이미지를 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmpat.html>.

- 지정된 패턴과 크기로 PPM 파일 생성:

`ppmpat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gingham2|gingham3|madras|tartan|poles|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- 지정된 색상으로 위장 패턴의 PPM 파일 생성:

`ppmpat -camo -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상1,색상2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>
