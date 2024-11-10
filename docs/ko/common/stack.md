---
layout: page
title: common/stack (한국어)
description: "Haskell 프로젝트 관리 도구."
content_hash: 89a5eae8920ada431012cca02fda6c00b27b3aae
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stack

Haskell 프로젝트 관리 도구.
더 많은 정보: <https://github.com/commercialhaskell/stack>.

- 새 패키지 생성:

`stack new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿</span>

- 패키지 컴파일:

`stack build`

- 패키지 내 테스트 실행:

`stack test`

- 프로젝트를 컴파일하고 파일이 변경될 때마다 다시 컴파일:

`stack build --file-watch`

- 프로젝트 컴파일 후 명령 실행:

`stack build --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 프로그램을 실행하고 인수를 전달:

`stack exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>
