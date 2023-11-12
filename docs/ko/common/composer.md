---
layout: page
title: common/composer (한국어)
description: "PHP 프로젝트의 의존성(dependency)을 기반으로 한 매니저 패키지."
content_hash: 24112041720993a6cb5f056ff393735faa0322d3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/composer.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># composer

PHP 프로젝트의 의존성(dependency)을 기반으로 한 매니저 패키지.
더 많은 정보: <https://getcomposer.org/>.

- 프로젝트의 의존성(dependency)으로 패키지를 추가합니다, 다음에 추가합니다 `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/패키지명</span>

- 프로젝트의 `composer.json` 안에 모든 의존성(dependency)를 설치합니다:

`composer install`

- 프로젝트의 패키지를 제거하며 `composer.json` 안의 모든 의존성(dependency)를 제거합니다:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/패키지명</span>

- 프로젝트의 `composer.json` 파일의 모든 의존성(dependency)를 업데이트 합니다:

`composer update`

- composer를 최신 버전으로 업데이트 합니다:

`composer self-update`
