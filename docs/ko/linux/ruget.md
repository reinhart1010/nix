---
layout: page
title: linux/ruget (한국어)
description: "Rust로 작성된 wget의 대안 도구."
content_hash: 3f6d09ce09789497ba8a646232f23d133a29fe6d
last_modified_at: 2024-11-10
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
tldri18n_status: 2
---
# ruget

Rust로 작성된 wget의 대안 도구.
더 많은 정보: <https://github.com/ksk001100/ruget>.

- URL의 콘텐츠를 파일로 다운로드:

`ruget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file</span>

- URL의 콘텐츠를 지정한 [o]출력 파일로 다운로드:

`ruget --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file</span>
