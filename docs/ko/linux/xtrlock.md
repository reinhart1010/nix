---
layout: page
title: linux/xtrlock (한국어)
description: "사용자가 비밀번호를 입력할 때까지 X 디스플레이를 잠급니다."
content_hash: adc7f87bba8a395de0e41972643187a936c76986
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xtrlock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xtrlock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xtrlock

사용자가 비밀번호를 입력할 때까지 X 디스플레이를 잠급니다.
더 많은 정보: <https://manned.org/xtrlock>.

- 디스플레이를 잠그고 커서 대신 자물쇠 아이콘 표시:

`xtrlock`

- 빈 화면과 자물쇠 커서를 표시:

`xtrlock -b`

- xtrlock 프로세스를 포크하고 즉시 반환:

`xtrlock -f`
