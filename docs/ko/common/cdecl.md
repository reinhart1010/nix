---
layout: page
title: common/cdecl (한국어)
description: "C 및 C++ 타입 선언을 작성하고 디코딩."
content_hash: c6c8e5d614a978537615971ba27a731cac6e420f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/cdecl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cdecl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cdecl

C 및 C++ 타입 선언을 작성하고 디코딩.
더 많은 정보: <https://github.com/paul-j-lucas/cdecl>.

- 영어 구문을 C 선언으로 작성하고, 컴파일 가능한([c]ompilable) 출력을 생성 (`;` 및 `{}` 포함):

`cdecl -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구문</span>

- C 선언을 영어로 설명:

`cdecl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C_선언</span>

- 변수를 다른 타입으로 캐스팅:

`cdecl cast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_이름</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>

- 대화형([i]nteractive) 모드에서 실행:

`cdecl -i`
