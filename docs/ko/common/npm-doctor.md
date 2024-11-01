---
layout: page
title: common/npm-doctor (한국어)
description: "npm 환경의 상태를 점검."
content_hash: b7c4ab4612b19de51ec73ceae78fc08e0e16006b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-doctor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-doctor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm doctor

npm 환경의 상태를 점검.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-doctor>.

- `npm`의 기본 상태 점검 수행:

`npm doctor`

- `npm` 레지스트리와의 연결 점검:

`npm doctor connection`

- 사용 중인 Node.js 및 `npm` 버전 점검:

`npm doctor versions`

- `npm` 디렉토리와 캐시의 권한 문제 점검:

`npm doctor permissions`

- 캐시된 패키지 파일과 체크섬 검증:

`npm doctor cache`
