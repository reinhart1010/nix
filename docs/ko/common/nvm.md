---
layout: page
title: common/nvm (한국어)
description: "Node.js 버전을 설치, 제거 또는 전환."
content_hash: 409bb0f36500b2118938937f6b4026d8347a562d
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/nvm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvm

Node.js 버전을 설치, 제거 또는 전환.
"12.8" 또는 "v16.13.1" 같은 버전 번호와 "stable", "system" 같은 레이블을 지원.
같이 보기: `asdf`.
더 많은 정보: <https://github.com/creationix/nvm>.

- 특정 버전의 Node.js 설치:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 현재 셸에서 특정 버전의 Node.js 사용:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 기본 Node.js 버전 설정:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 지정된 Node.js 버전 제거:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 특정 버전의 Node.js REPL 실행:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>` --version`

- 특정 버전의 Node.js에서 스크립트 실행:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
