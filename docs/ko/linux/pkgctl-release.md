---
layout: page
title: linux/pkgctl-release (한국어)
description: "빌드 아티팩트를 커밋, 태그 및 업로드하는 릴리스 단계."
content_hash: 8280974ffed51cef2a8d6a867925f9ff672eb9b6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkgctl-release.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pkgctl-release.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkgctl-release.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgctl release

빌드 아티팩트를 커밋, 태그 및 업로드하는 릴리스 단계.
더 많은 정보: <https://manned.org/pkgctl-release.1>.

- 빌드 아티팩트를 릴리스:

`pkgctl release --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_메시지</span>
