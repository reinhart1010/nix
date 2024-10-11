---
layout: page
title: common/docker-rm (한국어)
description: "컨테이너 제거."
content_hash: c8ede8234bc0fee81dce12c50e8964a9ceff0bcf
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker rm

컨테이너 제거.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- 컨테이너 제거:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너1 컨테이너2 ...</span>

- 컨테이너 강제 제거:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너1 컨테이너2 ...</span>

- 컨테이너와 그 볼륨 제거:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- 도움말 표시:

`docker rm --help`
