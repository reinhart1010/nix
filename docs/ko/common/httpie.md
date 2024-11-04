---
layout: page
title: common/httpie (한국어)
description: "HTTPie용 관리 인터페이스."
content_hash: 2e028201ff31d2b04b4335e17ab87a2f087cbeeb
last_modified_at: 2024-11-04
related_topics:
  - title: Deutsch version
    url: /de/common/httpie.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/httpie.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/httpie.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httpie.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httpie

HTTPie용 관리 인터페이스.
참조: `http`, 도구 자체.
더 많은 정보: <https://httpie.io/docs/cli/plugin-manager>.

- `http` 업데이트를 확인:

`httpie cli check-updates`

- 설치된 `http` 플러그인 목록 나열:

`httpie cli plugins list`

- 플러그인 설치/업그레이드/제거:

`httpie cli plugins `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설치|업그레이드|제거</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>
