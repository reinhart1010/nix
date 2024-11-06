---
layout: page
title: common/pambrighten (한국어)
description: "PAM 이미지의 채도와 명도를 변경."
content_hash: 0bc09e30eca021849da4648c02871918e594254d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pambrighten.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pambrighten.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pambrighten.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pambrighten

PAM 이미지의 채도와 명도를 변경.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- 각 픽셀의 채도를 지정된 백분율만큼 증가:

`pambrighten -saturation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백분율_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 각 픽셀의 명도(HSV 색상 공간에서)를 지정된 백분율만큼 증가:

`pambrighten -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백분율_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
