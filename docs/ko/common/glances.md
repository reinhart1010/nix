---
layout: page
title: common/glances (한국어)
description: "크로스 플랫폼 시스템 모니터링 도구."
content_hash: e0c116f25f5753ce094085103e0da533c8255bf4
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/glances.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glances.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glances

크로스 플랫폼 시스템 모니터링 도구.
더 많은 정보: <https://nicolargo.github.io/glances/>.

- 터미널에서 실행:

`glances`

- 웹 서버 모드에서 실행하여 브라우저에 결과를 표시:

`glances -w`

- other Glances 클라이언트의 연결을 허용하려면 서버 모드에서 실행:

`glances -s`

- Glances 서버에 연결:

`glances -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- (웹) 서버 모드에서 비밀번호가 필요:

`glances -s --password`
