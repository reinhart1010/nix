---
layout: page
title: common/rails-generate (한국어)
description: "기존 프로젝트에서 새로운 Rails 템플릿 생성."
content_hash: bdba591093142947b28b6a37b3d42fb6a67b9dfc
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rails-generate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-generate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rails-generate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rails-generate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rails generate

기존 프로젝트에서 새로운 Rails 템플릿 생성.
더 많은 정보: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- 사용 가능한 모든 생성기 나열:

`rails generate`

- 제목과 본문 속성을 가진 Post라는 새로운 모델 생성:

`rails generate model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body:text</span>

- index, show, new, create 액션을 가진 Posts라는 새로운 컨트롤러 생성:

`rails generate controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Posts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">create</span>

- 기존 모델 Post에 category 속성을 추가하는 새로운 마이그레이션 생성:

`rails generate migration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AddCategoryToPost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category:string</span>

- 제목과 본문 속성을 미리 정의하여 Post라는 모델을 위한 스캐폴드 생성:

`rails generate scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body:text</span>
