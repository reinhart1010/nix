---
layout: page
title: common/zapier-push (한국어)
description: "Zapier 통합을 빌드하고 업로드."
content_hash: ee65d8cb514c641a04f8570bb38ba86f736ba464
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zapier-push.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier push

Zapier 통합을 빌드하고 업로드.
더 많은 정보: <https://platform.zapier.com/reference/cli#push>.

- Zapier에 통합 푸시:

`zapier push`

- 스마트 파일 포함 비활성화 (`index.js`에 필요한 파일만 포함):

`zapier push --disable-dependency-detection`

- 추가 디버깅 출력 표시:

`zapier push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
