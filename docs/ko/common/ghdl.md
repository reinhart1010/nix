---
layout: page
title: common/ghdl (한국어)
description: "VHDL 언어용 오픈 소스 시뮬레이터."
content_hash: 050e1b88c789e82b58f182ea1f703c88b3a71277
last_modified_at: 2024-10-22
related_topics:
  - title: English version
    url: /en/common/ghdl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ghdl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghdl

VHDL 언어용 오픈 소스 시뮬레이터.
더 많은 정보: <https://ghdl.github.io/ghdl/>.

- VHDL 소스 파일을 분석하고 개체 파일을 생성:

`ghdl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.vhdl</span>

- 설계를 정교화 (여기서 `design`은 구성 단위, 엔터티 단위 또는 아키텍처 단위의 이름):

`ghdl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디자인</span>

- 정교한 디자인 실행:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디자인</span>

- 정교한 설계를 실행하고 출력을 파형 파일로 덤프:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디자인</span>` --wave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.ghw</span>

- VHDL 소스 파일의 구문을 확인:

`ghdl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.vhdl</span>

- 도움말 표시:

`ghdl --help`
