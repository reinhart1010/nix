---
layout: page
title: common/pnmtopclxl (한국어)
description: "PNM 파일을 HP LaserJet PCL XL 프린터 스트림으로 변환."
content_hash: 67bc57f1c50676db1001ad5f33c250c21dc8eb46
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtopclxl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtopclxl

PNM 파일을 HP LaserJet PCL XL 프린터 스트림으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtopclxl.html>.

- PNM 파일을 HP LaserJet PCL XL 프린터 스트림으로 변환:

`pnmtopclxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.pnm 경로/대상/입력2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pclxl</span>

- 이미지의 해상도와 각 이미지의 왼쪽 위 모서리에서 페이지의 위치를 지정:

`pnmtopclxl -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해상도</span>` -xoffs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_오프셋</span>` -yoffs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_오프셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.pnm 경로/대상/입력2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pclxl</span>

- 지정된 용지 형식에 대해 양면 프린터 스트림 생성:

`pnmtopclxl -duplex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세로|가로</span>` -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">letter|legal|a3|a4|a5|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.pnm 경로/대상/입력2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pclxl</span>
