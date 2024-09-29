---
layout: page
title: common/core-validate-commit (한국어)
description: "Node.js 코어에 대한 커밋 메시지를 확인."
content_hash: bf2bc1b72059b168de8c6505bd28e92e8291e277
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/core-validate-commit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/core-validate-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># core-validate-commit

Node.js 코어에 대한 커밋 메시지를 확인.
더 많은 정보: <https://github.com/nodejs/core-validate-commit>.

- 현재 커밋을 확인:

`core-validate-commit`

- 특정 커밋을 확인:

`core-validate-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해쉬</span>

- 다양한 커밋의 유효성을 검사:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해쉬</span>`..HEAD | xargs core-validate-commit`

- 모든 유효성 검사 규칙을 나열:

`core-validate-commit --list`

- 유효한 Node.js 하위시스템을 모두 나열:

`core-validate-commit --list-subsystem`

- 탭 형식으로 출력 형식을 지정하는 현재 커밋의 유효성을 검사:

`core-validate-commit --tap`

- 도움말 표시:

`core-validate-commit --help`
