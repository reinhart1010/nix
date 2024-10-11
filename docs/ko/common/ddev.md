---
layout: page
title: common/ddev (한국어)
description: "PHP 환경을 위한 컨테이너 기반 로컬 개발도구."
content_hash: f6aca0645ed17990e764df7fde122e4352651738
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/ddev.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ddev.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ddev

PHP 환경을 위한 컨테이너 기반 로컬 개발도구.
더 많은 정보: <https://ddev.readthedocs.io>.

- 프로젝트 시작:

`ddev start`

- 프로젝트 유형 및 문서 루트를 구성:

`ddev config`

- 로그를 계속해서 출력([f]ollow):

`ddev logs -f`

- 컨테이너 내에서 composer를 실행:

`ddev composer`

- 특정 Node.js 버전 설치:

`ddev nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 데이터베이스 내보내기:

`ddev export-db --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/db.sql.gz</span>

- 컨테이너 내에서 특정 명령을 실행:

`ddev exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 1</span>
