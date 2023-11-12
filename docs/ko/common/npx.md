---
layout: page
title: common/npx (한국어)
description: "`npm` 패키지에서 바이너리 실행."
content_hash: 0e1ade0f18a3371afb5602cdf741c6b46fe6c5f6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/npx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npx

`npm` 패키지에서 바이너리 실행.
더 많은 정보: <https://github.com/npm/npx>.

- 로컬 또는 원격 `npm` 패키지에서 명령을 실행:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자1 인자2 ...</span>

- 동일한 이름의 명령어가 여러 개 존재하는 경우, 패키지를 명시적으로 지정:

`npx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 현재 경로나 `node_modules/.bin`에 명령이 있는 경우 명령을 실행:

`npx --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자1 인자2 ...</span>

- `npx` 자체의 출력을 억제하는 특정 명령을 실행:

`npx --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자1 인자2 ...</span>

- 도움말 표시:

`npx --help`
