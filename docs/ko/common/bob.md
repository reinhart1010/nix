---
layout: page
title: common/bob (한국어)
description: "Neovim 버전을 관리하고 전환."
content_hash: 5b96527a2e3e1bf9567d294c85bd1eaecd693104
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/bob.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/bob.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bob

Neovim 버전을 관리하고 전환.
더 많은 정보: <https://github.com/MordechaiHadad/bob>.

- 지정된 버전의 Neovim을 설치하고 전환:

`bob use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- Neovim의 설치 및 현재 사용되는 버전을 출력:

`bob list`

- 특정 버전의 Neovim을 제거:

`bob uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- Neovim을 제거하고 `bob`이 변경한 내용을 모두 삭제:

`bob erase`

- 이전에 최신으로 수정된 버전으로 롤백:

`bob rollback`
