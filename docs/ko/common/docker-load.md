---
layout: page
title: common/docker-load (한국어)
description: "파일 또는 `stdin`에서 Docker 이미지를 로드합니다."
content_hash: 7c149db71bd85b741133a39c4bfb96524dd19128
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/docker-load.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-load.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-load.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-load.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker load

파일 또는 `stdin`에서 Docker 이미지를 로드합니다.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/load/>.

- `stdin`에서 Docker 이미지 로드:

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일.tar</span>

- 특정 파일에서 Docker 이미지 로드:

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일.tar</span>

- 조용한 모드로 특정 파일에서 Docker 이미지 로드:

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일.tar</span>
