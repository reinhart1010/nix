---
layout: page
title: common/expr (한국어)
description: "표현식을 평가하고 문자열을 조작."
content_hash: 12632abbb0eecb82c51c3b95ad428a67557032ea
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/expr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/expr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expr

표현식을 평가하고 문자열을 조작.
더 많은 정보: <https://www.gnu.org/software/coreutils/expr>.

- 특정 문자열의 길이를 가져옴:

`expr length "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`"`

- 특정 길이의 문자열의 하위 문자열을 가져옴:

`expr substr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>

- 고정된 패턴과 특정 하위 문자열을 일치시킴:

`expr match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`'`

- 문자열의 특정 세트에서 첫 번째 문자 위치를 가져옴:

`expr index "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자</span>`"`

- 특정 수학적 표현을 계산:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|*|/|%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식2</span>

- 값이 0이 아니며 null이 아닌 경우, 첫 번째 표현식을 가져오고, 그렇지 않으면 두 번째 표현식을 가져옴:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식1</span>` \| `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식2</span>

- 두 표현식이 모두 0이 아니고 null이 아닌 경우, 첫 번째 표현식을 가져오고 그렇지 않으면 0을 얻음:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식1</span>` \& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식2</span>
