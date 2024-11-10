---
layout: page
title: common/tig (한국어)
description: "설정 가능한 `ncurses` 기반 Git TUI."
content_hash: aed9ca9196ca0214603dcee0ee4a91798f675e05
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/tig.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tig

설정 가능한 `ncurses` 기반 Git TUI.
같이 보기: `gitui`, `git-gui`.
더 많은 정보: <https://jonas.github.io/tig/doc/manual.html>.

- 현재 커밋부터 시작하여 시간 역순으로 커밋 순서 표시:

`tig`

- 특정 브랜치의 히스토리 표시:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>

- 특정 파일 또는 폴더의 히스토리 표시:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 ...</span>

- 두 참조(예: 브랜치 또는 태그) 간의 차이 표시:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기준_참조</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비교_참조</span>

- 모든 브랜치와 스태시의 커밋 표시:

`tig --all`

- 스태시 보기에서 시작하여 저장된 모든 스태시 표시:

`tig stash`

- TUI에서 도움말 표시:

`h`
