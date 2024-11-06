---
layout: page
title: common/julia (한국어)
description: "기술 컴퓨팅을 위한 고수준, 고성능 동적 프로그래밍 언어."
content_hash: 30fb7a505152e8e676f719d79ace822969e40375
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/julia.html
    icon: bi bi-globe
tldri18n_status: 2
---
# julia

기술 컴퓨팅을 위한 고수준, 고성능 동적 프로그래밍 언어.
더 많은 정보: <https://docs.julialang.org/en/v1/manual/getting-started/>.

- REPL(대화형 셸) 시작:

`julia`

- Julia 프로그램 실행 후 종료:

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램.jl</span>

- 인자를 받는 Julia 프로그램 실행:

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램.jl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자_목록</span>

- Julia 코드를 포함한 문자열 평가:

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">julia_코드</span>`'`

- 인자를 전달하며 Julia 코드 문자열 평가:

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">for x in ARGS; println(x); end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자_목록</span>

- 표현식을 평가하고 결과 출력:

`julia -E '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(1 - cos(pi/4))/2</span>`'`

- N개의 스레드를 사용하여 멀티스레드 모드로 Julia 시작:

`julia -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>
