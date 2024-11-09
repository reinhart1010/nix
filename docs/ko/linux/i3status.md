---
layout: page
title: linux/i3status (한국어)
description: "i3 윈도우 관리자를 위한 상태 줄."
content_hash: 8e29f2c70585e46fde1b4f554e461bbd2bd6379e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/i3status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/i3status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># i3status

i3 윈도우 관리자를 위한 상태 줄.
이 명령은 일반적으로 i3 구성 파일에서 호출됩니다.
더 많은 정보: <https://i3wm.org/i3status/manpage.html>.

- 기본 설정을 사용하여 주기적으로 상태 줄을 `stdout`에 출력:

`i3status`

- 특정 설정 파일을 사용하여 주기적으로 상태 줄을 `stdout`에 출력:

`i3status -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/i3status.conf</span>

- 도움말 및 버전 표시:

`i3status -h`
