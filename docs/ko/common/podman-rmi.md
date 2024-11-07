---
layout: page
title: common/podman-rmi (한국어)
description: "Podman 이미지 제거."
content_hash: c88e96169a8763b7236d8f4443d9a8fac333b18a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/podman-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/podman-rmi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># podman rmi

Podman 이미지 제거.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- 이름을 지정하여 하나 이상의 이미지 제거:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지2:태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- 강제로 이미지 제거:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 태그되지 않은 부모를 삭제하지 않고 이미지 제거:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 도움말 표시:

`podman rmi`
