---
layout: page
title: common/podman-image (한국어)
description: "Docker 이미지 관리."
content_hash: 22f5f5157905da24a2df0831039e4779fe03bd85
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/podman-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-image.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/podman-image.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># podman image

Docker 이미지 관리.
같이 보기: `podman build`, `podman import`, `podman pull`.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- 로컬 Docker 이미지 나열:

`podman image ls`

- 사용되지 않는 로컬 Docker 이미지 삭제:

`podman image prune`

- 모든 사용되지 않는 이미지 삭제 (태그가 없는 이미지뿐만 아니라):

`podman image prune --all`

- 로컬 Docker 이미지의 히스토리 표시:

`podman image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>
