---
layout: page
title: linux/ruget (한국어)
description: "Rust로 작성된 wget의 대안 도구."
content_hash: 3f6d09ce09789497ba8a646232f23d133a29fe6d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ruget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/ruget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/ruget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/ruget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ruget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruget

Rust로 작성된 wget의 대안 도구.
더 많은 정보: <https://github.com/ksk001100/ruget>.

- URL의 콘텐츠를 파일로 다운로드:

`ruget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file</span>

- URL의 콘텐츠를 지정한 [o]출력 파일로 다운로드:

`ruget --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file</span>
