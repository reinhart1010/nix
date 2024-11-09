---
layout: page
title: linux/kde-inhibit (한국어)
description: "명령어 실행 중 데스크탑의 다양한 기능을 억제."
content_hash: 6e814af34925e4098b6142ece44a2e62e68d2cdb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kde-inhibit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kde-inhibit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kde-inhibit

명령어 실행 중 데스크탑의 다양한 기능을 억제.
더 많은 정보: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- 전원 관리 억제:

`kde-inhibit --power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 화면 보호기 억제:

`kde-inhibit --screenSaver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- VLC를 실행하고, 실행 중 색 보정(야간 모드)을 억제:

`kde-inhibit --colorCorrect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vlc</span>
