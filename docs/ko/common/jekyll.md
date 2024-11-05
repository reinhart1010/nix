---
layout: page
title: common/jekyll (한국어)
description: "간단하고 블로그 친화적인 정적 사이트 생성기."
content_hash: 9cbfabb05a5cc8f07afa55a7c6ab14eac50dd7a6
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jekyll.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jekyll.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/jekyll.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jekyll.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jekyll

간단하고 블로그 친화적인 정적 사이트 생성기.
더 많은 정보: <https://jekyllrb.com/docs/usage/>.

- http://localhost:4000/ 에서 실행되는 개발 서버 생성:

`jekyll serve`

- 증분 재생성 활성화:

`jekyll serve --incremental`

- 자세한 출력 활성화:

`jekyll serve --verbose`

- 현재 디렉토리를 `./_site`로 생성:

`jekyll build`

- 사이트 정리 (사이트 출력 및 `cache` 디렉토리를 제거) 빌드 없이:

`jekyll clean`
