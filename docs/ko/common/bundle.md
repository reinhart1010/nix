---
layout: page
title: common/bundle (한국어)
description: "Ruby 프로그래밍 언어의 종속성 관리자."
content_hash: 9a25662a5ce545a97b35527f714c72e05d5e2d98
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bundle

Ruby 프로그래밍 언어의 종속성 관리자.
더 많은 정보: <https://bundler.io/man/bundle.1.html>.

- 작업 디렉토리에 있는 `Gemfile`에 정의된 모든 gem을 설치:

`bundle install`

- 현재 번들의 컨텍스트에서 명령을 실행:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자</span>

- `Gemfile` 에 정의된 규칙에 따라 모든 gem을 업데이트 하고 `Gemfile.lock`을 재생성:

`bundle update`

- `Gemfile`에 정의된 하나 이상의 특정 gem을 업데이트:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_이름2</span>

- `Gemfile`에 정의된 하나 이상의 특정 gem을 다음 패치 버전으로만 업데이트:

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_이름2</span>

- `Gemfile`에서 지정된 그룹 내의 모든 gem을 업데이트:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">development</span>

- 최신 버전이 있는 `Gemfile`에 설치된 gem을 나열:

`bundle outdated`

- 새로운 gem 스켈레톤을 생성:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_이름</span>
