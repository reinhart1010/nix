---
layout: page
title: common/lambo-new (한국어)
description: "Laravel과 Valet을 위한 강력한 `laravel new`."
content_hash: a7e2858af8eef92fb3da20253c9c17eaf422fca9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lambo-new.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lambo new

Laravel과 Valet을 위한 강력한 `laravel new`.
더 많은 정보: <https://github.com/tighten/lambo>.

- 새로운 Laravel 애플리케이션 생성:

`lambo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 특정 경로에 애플리케이션 설치:

`lambo new --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 인증 스캐폴딩 포함:

`lambo new --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 특정 프론트엔드 포함:

`lambo new --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vue|bootstrap|react</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 프로젝트 생성 후 `npm` 종속성 설치:

`lambo new --node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 프로젝트 생성 후 Valet 사이트 생성:

`lambo new --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 프로젝트와 동일한 이름의 새 MySQL 데이터베이스 생성:

`lambo new --create-db --dbuser=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --dbpassword=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 프로젝트 생성 후 특정 편집기 열기:

`lambo new --editor="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">편집기</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>
