---
layout: page
title: common/pnpx (한국어)
description: "npm 패키지의 바이너리를 `npm` 대신 `pnpm`을 사용하여 직접 실행."
content_hash: 980a74626c20d90bc57617abf8402fb2d0061f9c
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pnpx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnpx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnpx

npm 패키지의 바이너리를 `npm` 대신 `pnpm`을 사용하여 직접 실행.
참고: 이 명령은 사용이 중단되었습니다! 대신 `pnpm exec` 및 `pnpm dlx`를 사용하세요.
더 많은 정보: <https://cuyl.github.io/pnpm.github.io/pnpx-cli>.

- 주어진 `npm` 모듈에서 바이너리 실행:

`pnpx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 주어진 `npm` 모듈이 여러 바이너리를 포함하는 경우 특정 바이너리 실행:

`pnpx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 도움말 표시:

`pnpx --help`
