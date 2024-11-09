---
layout: page
title: linux/just.js (한국어)
description: "Linux용 V8 JavaScript 런타임."
content_hash: ae2d32aeb6796c8a47cbb43a37249b37938390fe
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/just.js.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/just.js.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/just.js.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># just

Linux용 V8 JavaScript 런타임.
더 많은 정보: <https://github.com/just-js/just>.

- REPL(대화형 셸) 시작:

`just`

- JavaScript 파일 실행:

`just `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- JavaScript 코드를 인수로 전달하여 평가:

`just eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 동일한 이름의 디렉터리에 새 프로젝트 초기화:

`just init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- JavaScript 애플리케이션을 실행 파일로 빌드:

`just build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>` --static`
