---
layout: page
title: common/k8s-unused-secret-detector (한국어)
description: "사용되지 않는 Kubernetes 시크릿 감지."
content_hash: 05e4d7cc51cc972f547b777ba9d0b25eb0ee1db7
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/k8s-unused-secret-detector.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/k8s-unused-secret-detector.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># k8s-unused-secret-detector

사용되지 않는 Kubernetes 시크릿 감지.
더 많은 정보: <https://github.com/dtan4/k8s-unused-secret-detector>.

- 사용되지 않는 시크릿 감지:

`k8s-unused-secret-detector`

- 특정 네임스페이스에서 사용되지 않는 시크릿 감지:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 특정 네임스페이스에서 사용되지 않는 시크릿 삭제:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>` | kubectl delete secret -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>
