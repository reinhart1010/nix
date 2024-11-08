---
layout: page
title: linux/delpart (한국어)
description: "Linux 커널에게 파티션을 잊도록 요청합니다."
content_hash: 8596033bc6f21e05234621a4a5d99599311cfb4c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/delpart.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/delpart.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># delpart

Linux 커널에게 파티션을 잊도록 요청합니다.
더 많은 정보: <https://manned.org/delpart>.

- 커널에게 `/dev/sda`의 첫 번째 파티션을 잊도록 요청:

`sudo delpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
