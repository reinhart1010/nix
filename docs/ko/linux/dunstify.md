---
layout: page
title: linux/dunstify (한국어)
description: "`notify-send`의 확장 기능을 가진 알림 도구로, `dunst`를 중심으로 더 많은 기능을 제공합니다."
content_hash: 4cb5cd64068e03c3785d75fc93de6fb3bd93bc5e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dunstify.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dunstify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dunstify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dunstify

`notify-send`의 확장 기능을 가진 알림 도구로, `dunst`를 중심으로 더 많은 기능을 제공합니다.
`notify-send`의 모든 옵션을 수용합니다.
더 많은 정보: <https://github.com/dunst-project/dunst/wiki/Guides>.

- 지정된 제목과 메시지로 알림 표시:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 지정된 긴급도로 알림 표시:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|normal|critical</span>

- 메시지 ID 지정 (같은 ID의 이전 메시지를 덮어씀):

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123</span>

- 도움말 표시:

`dunstify --help`
