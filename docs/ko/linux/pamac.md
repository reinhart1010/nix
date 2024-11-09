---
layout: page
title: linux/pamac (한국어)
description: "GUI 패키지 관리자 pamac의 명령줄 도구."
content_hash: e952be787bd8cff054dbe498634dcd12cd01518e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pamac.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pamac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pamac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamac

GUI 패키지 관리자 pamac의 명령줄 도구.
AUR 패키지가 보이지 않으면 `/etc/pamac.conf` 또는 GUI에서 활성화하세요.
더 많은 정보: <https://wiki.manjaro.org/index.php/Pamac>.

- 새 패키지 설치:

`pamac install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지 및 더 이상 필요하지 않은 의존성(고아) 제거:

`pamac remove --orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지 데이터베이스에서 패키지 검색:

`pamac search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 설치된 패키지 나열:

`pamac list --installed`

- 패키지 업데이트 확인:

`pamac checkupdates`

- 모든 패키지 업그레이드:

`pamac upgrade`
