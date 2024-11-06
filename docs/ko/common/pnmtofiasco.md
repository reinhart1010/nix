---
layout: page
title: common/pnmtofiasco (한국어)
description: "PNM 이미지를 압축된 FIASCO 파일로 변환."
content_hash: 7a159ef1ba3d6b8add8a4476c0996b206aa467a4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtofiasco.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtofiasco

PNM 이미지를 압축된 FIASCO 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtofiasco.html>.

- PNM 이미지를 압축된 FIASCO 파일로 변환:

`pnmtofiasco `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fiasco</span>

- 패턴을 통해 [i]nput 파일 지정:

`pnmtofiasco --image-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">img[01-09+1].pnm</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fiasco</span>

- 압축 품질 지정:

`pnmtofiasco --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">품질_수준</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fiasco</span>

- 지정된 구성 파일에서 사용할 옵션 로드:

`pnmtofiasco --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fiascorc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fiasco</span>
