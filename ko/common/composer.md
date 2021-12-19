---
layout: page
title: common/composer (한국어)
description: "PHP 프로젝트의 의존성(dependency)을 기반으로 한 매니저 패키지."
content_hash: f56ab2bd73d163e781934775a8d1605a6ef8e1dc
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/composer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># composer

PHP 프로젝트의 의존성(dependency)을 기반으로 한 매니저 패키지.
더 많은 정보: <https://getcomposer.org/>.

- 프로젝트의 의존성(dependency)으로 패키지를 추가합니다, 다음에 추가합니다 `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/패키지명</span>

- 프로젝트의 `composer.json` 안에 모든 의존성(dependency)를 설치합니다 :

`composer install`

- 프로젝트의 패키지를 제거하며 `composer.json` 안의 모든 의존성(dependency)를 제거합니다:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/패키지명</span>

- 프로젝트의 `composer.json` 파일의 모든 의존성(dependency)를 업데이트 합니다:

`composer update`

- composer를 최신 버전으로 업데이트 합니다:

`composer self-update`
