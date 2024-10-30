---
layout: page
title: common/hadolint (한국어)
description: "Dockerfile 린터."
content_hash: f0de3f8359ac4f741db2485b46c61230af2dd95d
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/hadolint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hadolint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hadolint

Dockerfile 린터.
더 많은 정보: <https://github.com/hadolint/hadolint>.

- Dockerfile 린트:

`hadolint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- Dockerfile을 린트하여, 출력을 JSON 형식으로 표시:

`hadolint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- Dockerfile을 린트하여, 특정 형식으로 출력을 표시:

`hadolint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty|json|checkstyle|codeclimate|codacy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- 특정 규칙을 무시하고 Dockerfile을 린트:

`hadolint --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DL3006</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DL3008</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- 특정 신뢰할 수 있는 레지스트리를 사용하여 여러 Dockerfile을 린트하는 것:

`hadolint --trusted-registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker.io</span>` --trusted-registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile1 경로/대상/Dockerfile2 ...</span>
