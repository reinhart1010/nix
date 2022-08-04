---
layout: page
title: common/bundle (한국어)
description: "Ruby 프로그래밍 언어의 종속성 관리자."
content_hash: a7eb75c7db1396dfffff84bc8afcca575af96da4
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bundle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bundle

Ruby 프로그래밍 언어의 종속성 관리자.
더 많은 정보: <https://bundler.io/man/bundle.1.html>.

- 작업 디렉토리에 있는 `Gemfile`에 정의된 모든 gem을 설치:

`bundle install`

- `Gemfile` 에 정의된 규칙에 따라 모든 gem을 업데이트 하고 `Gemfile.lock`을 재생성:

`bundle update`

- `Gemfile`에 정의된 특정 gem을 업데이트:

`bundle update --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem명</span>

- 새로운 gem의 스켈레톤 생성:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem명</span>
