---
layout: page
title: common/vim (한국어)
description: "Vim (Vi IMproved)는 커맨드 라인 텍스트 에디터로 다양한 종류의 텍스트 조작을 위해 여러 모드를 지원합니다."
content_hash: de80d1473b3046f4ccd5d38c98803a389286c65e
last_modified_at: 2023-11-12
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

Vim (Vi IMproved)는 커맨드 라인 텍스트 에디터로 다양한 종류의 텍스트 조작을 위해 여러 모드를 지원합니다.
`i` 를 눌러 입력 모드로 들어가고, `<Esc>` 를 눌러 Vim 명령어를 입력할 수 있는 일반 모드로 들어갑니다.
더 많은 정보: <https://www.vim.org>.

- 파일 열기:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- 지정된 줄 번호에서 파일 열기:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄 번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- Vim 메뉴얼 보기:

`:help<Enter>`

- 저장하고 종료:

`:wq<Enter>`

- 실행취소:

`u`

- 파일에서 패턴 검색 (`n`/`N` 을 눌러 다음/이전 항목으로 이동):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할_패턴</span>`<Enter>`

- 전체 파일에서 정규식 대체 수행:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식_표현</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바꿀_문자열</span>`/g<Enter>`

- 줄 번호 표시:

`:set nu<Enter>`
