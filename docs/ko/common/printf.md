---
layout: page
title: common/printf (한국어)
description: "텍스트를 형식화하여 출력."
content_hash: 51f0be91388b841def9ff96ea0cf3989cfdd3edd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/printf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/printf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# printf

텍스트를 형식화하여 출력.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- 텍스트 메시지 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello world</span>`"`

- 정수를 굵은 파란색으로 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\e[1;34m%.3d\e[0m\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- 유로 기호와 함께 실수 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\u20AC %.2f\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123.4</span>

- 환경 변수를 사용하여 구성된 텍스트 메시지 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var1: %s\tvar2: %s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR2</span>`"`

- 형식화된 메시지를 변수에 저장 (Zsh에서는 작동하지 않음):

`printf -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myvar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"This is %s = %d\n" "a year" 2016</span>

- 16진수, 8진수 및 과학적 표기법 숫자 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex=%x octal=%o scientific=%e</span>`" 0x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF</span>` 0`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">377</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>
