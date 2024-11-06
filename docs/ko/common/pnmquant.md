---
layout: page
title: common/pnmquant (한국어)
description: "PNM 이미지의 색상을 더 작은 세트로 양자화."
content_hash: 95667f947fd8b5964c5dc0cbdcb287e5b4709be3
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmquant.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmquant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmquant

PNM 이미지의 색상을 더 작은 세트로 양자화.
이 명령은 `pnmcolormap`과 `pnmremap`의 조합이며 `-mapfile`을 제외한 두 명령의 옵션을 모두 허용합니다.
같이 보기: `pnmquantall`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- 입력 이미지에 최대한 가깝게 `n_colors` 개 이하의 색상만 사용하여 이미지를 생성:

`pnmquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
