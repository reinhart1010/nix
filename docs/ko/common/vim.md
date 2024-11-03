---
layout: page
title: common/vim (한국어)
description: "Vim (Vi IMproved)는 다양한 텍스트 조작을 위한 여러 모드를 제공하는 명령줄 텍스트 편집기입니다."
content_hash: ed3ef6b782377ad1b54dd1af1772b54c2a477d08
last_modified_at: 2024-11-03
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

Vim (Vi IMproved)는 다양한 텍스트 조작을 위한 여러 모드를 제공하는 명령줄 텍스트 편집기입니다.
일반 모드에서 `i`를 눌러 삽입 모드로 진입합니다. `<Esc>`를 눌러 다시 일반 모드로 돌아가면 Vim 명령을 사용할 수 있습니다.
같이 보기: `vimdiff`, `vimtutor`, `nvim`.
더 많은 정보: <https://www.vim.org>.

- 파일 열기:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정한 줄 번호에서 파일 열기:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Vim 메뉴얼 보기:

`:help<Enter>`

- 현재 버퍼 저장 및 종료:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- 일반 모드로 전환하고 마지막 작업 취소:

`<Esc>u`

- 파일 내 패턴 검색 (`n`/`N`을 눌러 다음/이전 일치 항목으로 이동):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`<Enter>`

- 전체 파일에서 정규식 대체 수행:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식_표현</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바꿀_문자열</span>`/g<Enter>`

- 줄 번호 표시:

`:set nu<Enter>`
