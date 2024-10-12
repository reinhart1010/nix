---
layout: page
title: common/gh-config (한국어)
description: "GitHub CLI의 설정 변경."
content_hash: 214b8adb0cdbb6fd40c16eb8f59605e6771ba95c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh config

GitHub CLI의 설정 변경.
더 많은 정보: <https://cli.github.com/manual/gh_config>.

- 사용 중인 Git 프로토콜 표시:

`gh config get git_protocol`

- 프로토콜을 SSH로 설정:

`gh config set git_protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- 모든 `gh` 명령어의 기본 페이지로 `delta`를 나란히 보기 모드로 사용:

`gh config set pager '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delta --side-by-side</span>`'`

- 텍스트 편집기를 Vim으로 설정:

`gh config set editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>

- 기본 텍스트 편집기로 재설정:

`gh config set editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">""</span>

- 대화형 프롬프트 비활성화:

`gh config set prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disabled</span>

- 특정 설정 값 설정:

`gh config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
