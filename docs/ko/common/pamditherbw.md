---
layout: page
title: common/pamditherbw (한국어)
description: "그레이스케일 이미지에 디더링을 적용하여 원래의 그레이스케일과 동일하게 보이는 흑백 픽셀 패턴으로 변환."
content_hash: 3af8301498acc65a944fa1a35553a9f37948f94b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamditherbw.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamditherbw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamditherbw

그레이스케일 이미지에 디더링을 적용하여 원래의 그레이스케일과 동일하게 보이는 흑백 픽셀 패턴으로 변환.
같이 보기: `pbmreduce`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- PGM 이미지를 읽고 디더링을 적용하여 파일로 저장:

`ppmditherbw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pgm</span>

- 지정된 양자화 방법 사용:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">floyd|fs|atkinson|threshold|hilbert|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pgm</span>

- atkinson 양자화 방법과 지정된 시드를 사용하여 의사 난수 생성기 사용:

`ppmditherbw -atkinson -randomseed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1337</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pgm</span>

- 특정 형태의 임계값 처리를 수행하는 양자화 방법을 위한 임계값 지정:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fs|atkinson|thresholding</span>` -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pgm</span>
