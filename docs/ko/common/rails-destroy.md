---
layout: page
title: common/rails-destroy (한국어)
description: "Rails 리소스를 삭제."
content_hash: 4d044b153b04dad702cd696730af5a8c4eaf7343
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rails-destroy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-destroy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rails-destroy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rails destroy

Rails 리소스를 삭제.
더 많은 정보: <https://guides.rubyonrails.org/command_line.html#bin-rails-destroy>.

- 삭제 가능한 모든 생성기 나열:

`rails destroy`

- Post라는 이름의 모델 삭제:

`rails destroy model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>

- Posts라는 이름의 컨트롤러 삭제:

`rails destroy controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Posts</span>

- Posts를 생성하는 마이그레이션 삭제:

`rails destroy migration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CreatePosts</span>

- Post라는 이름의 모델에 대한 스캐폴드 삭제:

`rails destroy scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>
