---
layout: page
title: common/flex (한국어)
description: "어휘 분석기 생성기. POSIX 사양을 확장하여 `lex`."
content_hash: 26a993fcc3e131da51afe91f465d747c1163df7d
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/flex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flex

어휘 분석기 생성기. POSIX 사양을 확장하여 `lex`.
어휘 분석기에 대한 사양이 주어지면 이를 구현하는 C 코드를 생성.
참고: OpenBSD에서는 긴 옵션이 작동하지 않음.
더 많은 정보: <https://manned.org/flex>.

- flex 파일에서 분석기를 생성하여, `lex.yy.c` 파일에 저장:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- `stdout`에 분석기 쓰기:

`lex -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-stdout|t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- 출력 파일을 지정:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.c</span>

- 대화형 스캐너 대신 [B]atch 스캐너를 생성:

`lex -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Lex에서 생성된 C 파일을 컴파일:

`cc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/lex.yy.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>
