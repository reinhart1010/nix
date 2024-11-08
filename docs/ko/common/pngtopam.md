---
layout: page
title: common/pngtopam (한국어)
description: "PNG 이미지를 Netpbm 이미지로 변환."
content_hash: c3d017e0ad6134ed424f6dca4b4a1d444cdf0ae3
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pngtopam.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pngtopam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pngtopam

PNG 이미지를 Netpbm 이미지로 변환.
같이 보기: `pamtopng`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- 지정된 PNG 이미지를 Netpbm 이미지로 변환:

`pngtopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 입력 이미지의 주 이미지와 투명 마스크를 포함한 출력 이미지 생성:

`pngtopam -alphapam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 투명한 픽셀을 지정된 색상으로 대체:

`pngtopam -mix -background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 입력 이미지에서 발견된 tEXt 청크를 지정된 텍스트 파일로 작성:

`pngtopam -text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
