---
layout: page
title: linux/goobook (한국어)
description: "`mutt` 또는 명령줄에서 Google 연락처에 접근."
content_hash: 735f8247ae2cb6f5220e7c3bff6ea9756b8fe708
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/goobook.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/goobook.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># goobook

`mutt` 또는 명령줄에서 Google 연락처에 접근.
더 많은 정보: <https://manned.org/goobook>.

- OAuth2를 사용하여 `goobook`이 Google 연락처에 접근 허용:

`goobook authenticate`

- 모든 연락처를 XML 형식으로 출력(`stdout`):

`goobook dump_contacts`
