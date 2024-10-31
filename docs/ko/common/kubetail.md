---
layout: page
title: common/kubetail (한국어)
description: "여러 Kubernetes 포드의 로그를 동시에 추적하는 유틸리티."
content_hash: 259886fe692face361ed35d6cfc25c784554a923
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kubetail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubetail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubetail

여러 Kubernetes 포드의 로그를 동시에 추적하는 유틸리티.
더 많은 정보: <https://github.com/johanhaleby/kubetail>.

- 여러 포드의 로그를 한 번에 추적 (포드 이름이 "my_app"으로 시작하는 경우):

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>

- 여러 포드에서 특정 컨테이너의 로그만 추적:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container</span>

- 여러 포드에서 여러 컨테이너의 로그를 추적:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container_1</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container_2</span>

- 여러 애플리케이션의 로그를 동시에 추적하려면 쉼표로 구분:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app_2</span>
