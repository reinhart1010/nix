---
layout: page
title: common/pamcomp (한국어)
description: "두 개의 PAM 이미지를 오버레이."
content_hash: 097c182be1889ca818c062988796aa4576188e1a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamcomp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamcomp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamcomp

두 개의 PAM 이미지를 오버레이.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- 오버레이가 아래 부분을 가리도록 두 이미지를 오버레이:

`pamcomp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오버레이.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/언더레이.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 오버레이의 수평 정렬 설정:

`pamcomp -align `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|center|right|beyondleft|beyondright</span>` -xoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수평_오프셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오버레이.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/언더레이.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 오버레이의 수직 정렬 설정:

`pamcomp -valign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|middle|bottom|above|below</span>` -yoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수직_오프셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오버레이.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/언더레이.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 오버레이의 불투명도 설정:

`pamcomp -opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오버레이.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/언더레이.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
