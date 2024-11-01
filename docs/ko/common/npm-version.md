---
layout: page
title: common/npm-version (한국어)
description: "Node 패키지의 버전을 증가시킵니다."
content_hash: fde3f1e3a5b48f0c0952344f27f2014758edc0b1
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-version.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-version.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm version

Node 패키지의 버전을 증가시킵니다.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-version>.

- 현재 버전 확인:

`npm version`

- 마이너 버전 증가:

`npm version minor`

- 특정 버전 설정:

`npm version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Git 태그를 생성하지 않고 패치 버전 증가:

`npm version patch --no-git-tag-version`

- 사용자 정의 커밋 메시지와 함께 메이저 버전 증가:

`npm version major -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%s 이유로 업그레이드함</span>`"`
