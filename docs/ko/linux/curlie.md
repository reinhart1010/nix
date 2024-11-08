---
layout: page
title: linux/curlie (한국어)
description: "`curl`의 프론트엔드로, `httpie`의 사용 편의성을 추가합니다."
content_hash: c4d0fec1877bebc93c4d6e419ed6acb6446fbf64
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/curlie.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/curlie.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/curlie.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># curlie

`curl`의 프론트엔드로, `httpie`의 사용 편의성을 추가합니다.
더 많은 정보: <https://github.com/rs/curlie>.

- GET 요청 전송:

`curlie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>

- POST 요청 전송:

`curlie post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=john</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">age:=25</span>

- 쿼리 매개변수를 포함한 GET 요청 전송 (예: `first_param=5&second_param=true`):

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_param==5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_param==true</span>

- 사용자 정의 헤더와 함께 GET 요청 전송:

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header-name:header-value</span>
