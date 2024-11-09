---
layout: page
title: common/steamcmd (한국어)
description: "Steam 클라이언트의 커맨드라인 버전."
content_hash: 689b209a76d6ea46d3aa20195c8ee79f7a50b32b
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/steamcmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/steamcmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/steamcmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># steamcmd

Steam 클라이언트의 커맨드라인 버전.
더 많은 정보: <https://manned.org/steamcmd>.

- 익명으로 애플리케이션 설치 또는 업데이트:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">익명</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱ID</span>` +quit`

- 지정된 자격 증명을 사용하여 애플리케이션 설치 또는 업데이트:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱ID</span>` +quit`

- 특정 플랫폼용 애플리케이션 설치:

`steamcmd +@sSteamCmdForcePlatformType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows</span>` +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anonymous</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱ID</span>` validate +quit`
