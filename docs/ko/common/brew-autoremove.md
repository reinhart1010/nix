---
layout: page
title: common/brew-autoremove (한국어)
description: "이전에 종속성으로 설치되어 사용되지 않는 수식을 제거."
content_hash: bdec0ac7b0e0e86e94f1a65f391e80a938dd34c4
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/brew-autoremove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/brew-autoremove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-autoremove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew autoremove

이전에 종속성으로 설치되어 사용되지 않는 수식을 제거.
더 많은 정보: <https://docs.brew.sh/Manpage#autoremove---dry-run>.

- 사용하지 않는 수식을 모두 제거:

`brew autoremove`

- 제거할 항목을 인쇄하지만, 실제로 아무것도 제거하지 않음:

`brew autoremove --dry-run`
