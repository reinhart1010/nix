---
layout: page
title: common/stern (한국어)
description: "Kubernetes의 여러 팟 및 컨테이너 로그를 동시에 확인."
content_hash: 19c07e862ac4efbdf7340faeba29abf308e3cd34
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/stern.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stern.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stern

Kubernetes의 여러 팟 및 컨테이너 로그를 동시에 확인.
더 많은 정보: <https://github.com/stern/stern>.

- 현재 네임스페이스 내의 모든 팟 로그 확인:

`stern .`

- 특정 상태의 모든 팟 로그 확인:

`stern . --container-state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">running|waiting|terminated</span>

- 주어진 정규 표현식과 일치하는 모든 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>

- 모든 네임스페이스에서 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --all-namespaces`

- 15분 전부터 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15m</span>

- 특정 레이블이 있는 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --selector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release=canary</span>
