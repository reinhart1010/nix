---
layout: page
title: linux/systemd-repart (한국어)
description: "자동으로 파티션을 확장하고 추가."
content_hash: 7c136fb8217b6b9bf37c3e8355be427f9cf09409
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-repart.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-repart.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-repart

자동으로 파티션을 확장하고 추가.
repart.d에 설명된 구성 파일을 기반으로 파티션을 확장하고 추가합니다.
파티션의 파일 시스템 크기를 자동으로 조정하지 않습니다. 파일 시스템 확장을 위해 systemd-growfs를 참조하세요.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-repart.html>.

- 루트 파티션 (/)을 사용 가능한 모든 디스크 공간으로 확장:

`systemd-repart`

- 변경 사항을 적용하지 않고 보기:

`systemd-repart --dry-run=yes`

- 루트 파티션 크기를 10기가바이트로 확장:

`systemd-repart --size=10G --root /`
