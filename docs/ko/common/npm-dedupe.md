---
layout: page
title: common/npm-dedupe (한국어)
description: "`node_modules` 디렉토리에서 중복을 줄입니다."
content_hash: f2a44b7c69de9736a8980dd284e521f1fed39b1c
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-dedupe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-dedupe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm dedupe

`node_modules` 디렉토리에서 중복을 줄입니다.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-dedupe>.

- `node_modules`의 패키지 중복 제거:

`npm dedupe`

- 중복 제거 시 `package-lock.json` 또는 `npm-shrinkwrap.json`을 따르기:

`npm dedupe --lock`

- 엄격 모드로 중복 제거 실행:

`npm dedupe --strict`

- 중복 제거 시 선택적/피어 의존성 건너뛰기:

`npm dedupe --omit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional|peer</span>

- 문제 해결을 위한 자세한 로깅 활성화:

`npm dedupe --loglevel=verbose`

- 특정 패키지에 대해 중복 제거 제한:

`npm dedupe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>
