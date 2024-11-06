---
layout: page
title: common/ppmtompeg (한국어)
description: "MPEG-1 스트림 인코딩."
content_hash: 998e534f60c39543f970d18445c5d822246a37ba
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtompeg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtompeg

MPEG-1 스트림 인코딩.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

- 입력 및 출력을 지정하는 매개 변수 파일을 사용하여 MPEG-1 스트림 생성:

`ppmtompeg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매개_변수_파일</span>

- 지정된 번호의 GOP만 인코딩:

`ppmtompeg -gop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gop_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매개_변수_파일</span>

- 인코딩할 첫 번째 및 마지막 프레임 지정:

`ppmtompeg -frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫_프레임</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마지막_프레임</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매개_변수_파일</span>

- 여러 MPEG 프레임을 단일 MPEG-1 스트림으로 결합:

`ppmtompeg -combine_frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매개_변수_파일</span>
