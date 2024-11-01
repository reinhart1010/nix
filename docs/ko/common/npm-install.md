---
layout: page
title: common/npm-install (한국어)
description: "Node 패키지 설치."
content_hash: 05d9028d8520e49d4fee88dba461093e7e553247
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm install

Node 패키지 설치.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-install>.

- package.json에 나열된 의존성 설치:

`npm install`

- 특정 버전의 패키지를 다운로드하고 `package.json`의 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 최신 버전의 패키지를 다운로드하고 `package.json`의 개발 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- 최신 버전의 패키지를 다운로드하고 전역으로 설치:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>
