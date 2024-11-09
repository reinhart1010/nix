---
layout: page
title: common/skaffold (한국어)
description: "Kubernetes 애플리케이션의 지속적인 개발을 지원."
content_hash: e6681e3b100a3d4d70f4779f868040d1348f8e2d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/skaffold.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/skaffold.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># skaffold

Kubernetes 애플리케이션의 지속적인 개발을 지원.
더 많은 정보: <https://skaffold.dev>.

- 아티팩트 빌드:

`skaffold build -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">skaffold.yaml</span>

- 코드가 변경될 때마다 앱 빌드 및 배포:

`skaffold dev -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">skaffold.yaml</span>

- 파이프라인 파일 실행:

`skaffold run -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">skaffold.yaml</span>

- Skaffold 진단 실행:

`skaffold diagnose -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">skaffold.yaml</span>

- 아티팩트 배포:

`skaffold deploy -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">skaffold.yaml</span>
