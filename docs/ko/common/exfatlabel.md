---
layout: page
title: common/exfatlabel (한국어)
description: "exFAT 파일 시스템 레이블 가져오기 또는 설정."
content_hash: 4420b63e7704d9d02ba904dc2ee5daf8cb3e0afa
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/exfatlabel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exfatlabel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exfatlabel

exFAT 파일 시스템 레이블 가져오기 또는 설정.
더 많은 정보: <https://manned.org/exfatlabel>.

- 현재 파일 시스템 레이블을 표시:

`exfatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 파일 시스템 레이블을 설정:

`exfatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_라벨</span>
