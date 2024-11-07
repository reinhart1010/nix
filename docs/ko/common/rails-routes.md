---
layout: page
title: common/rails-routes (한국어)
description: "Rails 애플리케이션에서 경로를 나열."
content_hash: 429cba7ebf30be30b1cd6036e2ea804322671751
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rails-routes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-routes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rails-routes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rails routes

Rails 애플리케이션에서 경로를 나열.
더 많은 정보: <https://guides.rubyonrails.org/routing.html>.

- 모든 경로 나열:

`rails routes`

- 확장된 형식으로 모든 경로 나열:

`rails routes --expanded`

- URL 헬퍼 메서드 이름, HTTP 메서드 또는 URL 경로와 부분적으로 일치하는 경로 나열:

`rails routes -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts_path|GET|/posts</span>

- 지정된 컨트롤러에 매핑된 경로 나열:

`rails routes -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts|Posts|Blogs::PostsController</span>
