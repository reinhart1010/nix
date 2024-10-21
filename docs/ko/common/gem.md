---
layout: page
title: common/gem (한국어)
description: "Ruby 프로그래밍 언어용 패키지 관리자."
content_hash: 6e102917e79e02f323bb93b1c238a913e72374ce
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gem.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gem.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gem

Ruby 프로그래밍 언어용 패키지 관리자.
더 많은 정보: <https://guides.rubygems.org>.

- 원격 gem을 검색하고 사용 가능한 모든 버전을 표시:

`gem search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` --all`

- 최신 버전의 gem을 설치:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>

- 특정 버전의 gem을 설치:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- 일치하는 최신 (SemVer) 버전의 gem을 설치:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>` --version '~> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>`'`

- gem 업데이트:

`gem update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>

- 모든 로컬 gem을 나열:

`gem list`

- gem 제거:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>

- 특정 버전의 gem을 제거:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">젬_이름</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>
