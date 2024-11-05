---
layout: page
title: common/nvme (한국어)
description: "NVMe 저장소 사용자 공간 유틸리티."
content_hash: 5b904ab5ccd6ee996970693de190f4290c25a325
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nvme.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvme.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvme

NVMe 저장소 사용자 공간 유틸리티.
더 많은 정보: <https://github.com/linux-nvme/nvme-cli>.

- 모든 NVMe 장치 나열:

`sudo nvme list`

- 장치 정보 표시:

`sudo nvme smart-log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>
