---
layout: page
title: common/docker-pull (한국어)
description: "Docker 이미지를 레지스트리에서 다운로드."
content_hash: 43f43e87145731917251124c981525c48fd51dff
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/docker-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-pull.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-pull.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-pull.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker pull

Docker 이미지를 레지스트리에서 다운로드.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- 특정 Docker 이미지 다운로드:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 조용한 모드로 특정 Docker 이미지 다운로드:

`docker pull --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 Docker 이미지의 모든 태그 다운로드:

`docker pull --all-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 특정 플랫폼의 Docker 이미지 다운로드 (예: linux/amd64):

`docker pull --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux/amd64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 도움말 표시:

`docker pull --help`
