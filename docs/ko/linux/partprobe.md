---
layout: page
title: linux/partprobe (한국어)
description: "운영 체제 커널에 파티션 테이블 변경 사항을 알립니다."
content_hash: eba0f1336557711686dfc2db7aa448470243b99a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/partprobe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/partprobe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># partprobe

운영 체제 커널에 파티션 테이블 변경 사항을 알립니다.
더 많은 정보: <https://manned.org/partprobe>.

- 운영 체제 커널에 파티션 테이블 변경 사항 알림:

`sudo partprobe`

- 커널에 파티션 테이블 변경 사항을 알리고 장치 및 해당 파티션의 요약 표시:

`sudo partprobe --summary`

- 커널에 알리지 않고 장치 및 해당 파티션의 요약 표시:

`sudo partprobe --summary --dry-run`
