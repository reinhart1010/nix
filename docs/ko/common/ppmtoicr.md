---
layout: page
title: common/ppmtoicr (한국어)
description: "PPM 이미지를 NCSA ICR 형식으로 변환."
content_hash: b8be4e3ce639ed1211f299bae85db7eabec11e75
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtoicr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtoicr

PPM 이미지를 NCSA ICR 형식으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoicr.html>.

- PPM 이미지를 ICR 파일로 변환:

`ppmtoicr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.icr</span>

- 출력 이름을 지정하여 표시:

`ppmtoicr -windowname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.icr</span>

- 지정한 배율로 이미지 확대:

`ppmtoicr -expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배율</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.icr</span>

- 지정한 번호로 화면에 출력 표시:

`ppmtoicr -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.icr</span>
