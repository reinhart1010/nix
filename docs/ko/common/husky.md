---
layout: page
title: common/husky (한국어)
description: "네이티브 Git 훅을 쉽게 만들었습니다."
content_hash: e5e61f3fe9b930cdd062048afce1259fc940aa61
last_modified_at: 2023-10-23
related_topics:
  - title: English version
    url: /en/common/husky.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># husky

네이티브 Git 훅을 쉽게 만들었습니다.
더 많은 정보: <https://typicode.github.io/husky>.

- 현재 폴더에 Husky를 설치:

`husky install`

- Husky를 특정 폴더에 설치:

`husky install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 명령을 Git의 `pre-push` 훅으로 설정:

`husky set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.husky/pre-push</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>`"`

- 현재 `pre-commit` 훅에 특정 명령을 추가:

`husky add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.husky/pre-commit</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>`"`

- 현재 폴더에서 Husky 훅 제거:

`husky uninstall`

- 도움말 표시:

`husky`
