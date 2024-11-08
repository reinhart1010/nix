---
layout: page
title: linux/debuild (한국어)
description: "소스에서 Debian 패키지를 빌드합니다."
content_hash: f3ac0ea2d82442a5be92d5cf5fe7f4981188cf81
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/debuild.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debuild.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debuild

소스에서 Debian 패키지를 빌드합니다.
더 많은 정보: <https://manned.org/debuild.1>.

- 현재 디렉토리에서 패키지 빌드:

`debuild`

- 바이너리 패키지만 빌드:

`debuild -b`

- 패키지 빌드 후 lintian을 실행하지 않음:

`debuild --no-lintian`
