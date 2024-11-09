---
layout: page
title: linux/update-rc.d (한국어)
description: "System-V 스타일의 init 스크립트 링크를 설치하고 제거합니다."
content_hash: f66edcb9a24b0c577220f5f1002e4590e7196319
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/update-rc.d.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/update-rc.d.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># update-rc.d

System-V 스타일의 init 스크립트 링크를 설치하고 제거합니다.
Init 스크립트는 `/etc/init.d/`에 있습니다.
더 많은 정보: <https://manned.org/update-rc.d>.

- 서비스 설치:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` defaults`

- 서비스 활성화:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` enable`

- 서비스 비활성화:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` disable`

- 서비스를 강제로 제거:

`update-rc.d -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` remove`
