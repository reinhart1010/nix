---
layout: page
title: common/npm-find-dupes (한국어)
description: "`node_modules`에서 중복된 의존성을 식별."
content_hash: 2844f0fcf672d9de97b25a2a7d7dcfde097bb3fa
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-find-dupes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-find-dupes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm find-dupes

`node_modules`에서 중복된 의존성을 식별.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-find-dupes>.

- `node_modules` 내 모든 중복 패키지 나열:

`npm find-dupes`

- 중복 감지에 `devDependencies` 포함:

`npm find-dupes --include=dev`

- `node-modules`에서 특정 패키지의 모든 중복 인스턴스 나열:

`npm find-dupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 중복 감지에서 선택적 의존성 제외:

`npm find-dupes --omit=optional`

- 출력의 로그 레벨 설정:

`npm find-dupes --loglevel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">silent|error|warn|info|verbose</span>

- 중복 정보를 JSON 형식으로 출력:

`npm find-dupes --json`

- 중복 검색을 특정 스코프로 제한:

`npm find-dupes --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@스코프1,@스코프2</span>

- 특정 스코프를 중복 감지에서 제외:

`npm find-dupes --omit-scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@스코프1,@스코프2</span>
