---
layout: page
title: common/nodenv (한국어)
description: "Node.js 버전을 관리."
content_hash: 690bbca370b31e610e47b0c9fbf1dcde95240c60
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/nodenv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nodenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nodenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nodenv

Node.js 버전을 관리.
더 많은 정보: <https://github.com/nodenv/nodenv>.

- 특정 버전의 Node.js 설치:

`nodenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 사용 가능한 버전 목록 표시:

`nodenv install --list`

- 시스템 전체에서 특정 버전의 Node.js 사용:

`nodenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 디렉토리에서 특정 버전의 Node.js 사용:

`nodenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 현재 디렉토리에서 사용 중인 Node.js 버전 표시:

`nodenv version`

- 설치된 Node.js 명령의 위치 표시 (예: `npm`):

`nodenv which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
