---
layout: page
title: common/argon2 (한국어)
description: "Argon2 암호화 해시 계산."
content_hash: 2eddf9db17f6ce262a038bd30de4177c744fcad3
last_modified_at: 2023-12-17
related_topics:
  - title: English version
    url: /en/common/argon2.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/argon2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/argon2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># argon2

Argon2 암호화 해시 계산.
더 많은 정보: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- 기본 매개변수를 사용하여 비밀번호와 솔트를 사용하여 해시를 계산:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">솔트_문자</span>`"`

- 지정된 알고리즘을 사용하여 해시 계산:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">솔트_문자</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|i|id</span>

- 추가 정보 없이 출력 해시 표시:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">솔트_문자</span>`" -e`

- 주어진 반복 [t](시간), [m](메모리 사용량) 및 [p](병렬성 매개변수)를 사용하여 해시를 계산:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">솔트_문자</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
