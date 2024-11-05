---
layout: page
title: common/nvim (한국어)
description: "Neovim은 Vim을 기반으로 한 프로그래머용 텍스트 편집기로, 다양한 텍스트 조작을 위한 여러 모드를 제공합니다."
content_hash: ad2269e6782a6f9c5b90758d2f97c17752ebc10e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nvim.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvim.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvim

Neovim은 Vim을 기반으로 한 프로그래머용 텍스트 편집기로, 다양한 텍스트 조작을 위한 여러 모드를 제공합니다.
일반 모드에서 `i`를 누르면 입력 모드로 전환됩니다. `<Esc>`를 누르면 일반 모드로 돌아가며, 일반 텍스트 입력이 허용되지 않습니다.
같이 보기: `vim`, `vimtutor`, `vimdiff`.
더 많은 정보: <https://neovim.io>.

- 파일 열기:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 텍스트 편집 모드(입력 모드)로 전환:

`<Esc>i`

- 현재 줄을 복사("yank") 또는 잘라내기("delete") (붙여넣기는 `P`로 수행):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- 일반 모드로 전환하고 마지막 작업을 실행 취소:

`<Esc>u`

- 파일에서 패턴 검색 (다음/이전 일치 항목으로 이동하려면 `n`/`N`을 누름):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`<Enter>`

- 전체 파일에서 정규 표현식을 이용한 치환 수행:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체_문자열</span>`/g<Enter>`

- 일반 모드로 전환하고 파일을 저장(쓰기) 후 종료:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- 저장하지 않고 종료:

`<Esc>:q!<Enter>`
