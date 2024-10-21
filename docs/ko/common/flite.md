---
layout: page
title: common/flite (한국어)
description: "음성 합성 엔진."
content_hash: c0ae748d18e41a7f2b0cffbf2ea824d8d0dfb4cf
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/flite.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flite

음성 합성 엔진.
더 많은 정보: <http://www.festvox.org/flite/doc/>.

- 사용 가능한 모든 음성을 나열:

`flite -lv`

- 텍스트 문자열을 음성으로 변환:

`flite -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`"`

- 파일 내용을 음성으로 변환:

`flite -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 지정된 음성 사용:

`flite -voice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://경로/대상/파일이름.flitevox|url</span>

- 출력을 wav 파일에 저장:

`flite -voice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://경로/대상/파일이름.flitevox|url</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">츨력파일.wav</span>

- 버전 정보 표시:

`flite --version`
