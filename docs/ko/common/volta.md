---
layout: page
title: common/volta (한국어)
description: "Node.js 런타임, npm 및 Yarn 패키지 관리자 또는 npm에서 제공하는 바이너리를 설치하는 JavaScript 도구 관리자."
content_hash: d371c9dabc6aab22051b9b37ebc5643dacddf041
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/volta.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/volta.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># volta

Node.js 런타임, npm 및 Yarn 패키지 관리자 또는 npm에서 제공하는 바이너리를 설치하는 JavaScript 도구 관리자.
더 많은 정보: <https://volta.sh>.

- 설치된 모든 도구 나열:

`volta list`

- 최신 버전의 도구 설치:

`volta install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn|패키지_이름</span>

- 특정 버전의 도구 설치:

`volta install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn</span>`@version`

- 프로젝트에 사용할 도구 버전 선택 (`package.json`에 저장됨):

`volta pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn</span>`@version`

- 도움말 표시:

`volta help`

- 하위 명령에 대한 도움말 표시:

`volta help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fetch|install|uninstall|pin|list|completions|which|setup|run|help</span>
