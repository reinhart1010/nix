---
layout: page
title: common/tuckr (한국어)
description: "Rust로 작성된 도트파일 관리 도구."
content_hash: dbb21d229b6e433072f1b878bf07cf5897ada47e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tuckr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tuckr

Rust로 작성된 도트파일 관리 도구.
같이 보기: `chezmoi`, `vcsh`, `homeshick`, `stow`.
더 많은 정보: <https://github.com/RaphGL/Tuckr>.

- 도트파일 상태 확인:

`tuckr status`

- 모든 도트파일 시스템에 추가:

`tuckr add \*`

- 지정된 프로그램을 제외한 모든 도트파일 추가:

`tuckr add \* -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램2</span>

- 시스템에서 모든 도트파일 제거:

`tuckr rm \*`

- 프로그램 도트파일 추가 및 설정 스크립트 실행:

`tuckr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
