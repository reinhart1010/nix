---
layout: page
title: common/ppmshadow (한국어)
description: "PPM 이미지에 시뮬레이션된 그림자를 추가."
content_hash: 49077eb92cac47f791d5b3c3d6bad76a1cd154c7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmshadow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmshadow

PPM 이미지에 시뮬레이션된 그림자를 추가.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmshadow.html>.

- PPM 이미지에 시뮬레이션된 그림자 추가:

`ppmshadow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 이미지를 지정된 픽셀 수만큼 [b]블러 처리:

`ppmshadow -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 이미지의 왼쪽과 위쪽으로 시뮬레이션된 광원의 변위를 지정:

`ppmshadow -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">왼쪽_오프셋</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위쪽_오프셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
