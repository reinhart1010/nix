---
layout: page
title: common/josm (한국어)
description: "Java 8+용 확장 가능한 OpenStreetMap 편집기."
content_hash: 1cf4757f783a0afded1ee5ee898ee4479d4a7826
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/josm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/josm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># josm

Java 8+용 확장 가능한 OpenStreetMap 편집기.
더 많은 정보: <https://josm.openstreetmap.de/>.

- JOSM 시작:

`josm`

- JOSM을 최대화 모드로 시작:

`josm --maximize`

- JOSM을 특정 언어로 시작:

`josm --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>

- JOSM을 시작하고 모든 환경설정을 기본값으로 재설정:

`josm --reset-preferences`

- JOSM을 시작하고 특정 경계 상자를 다운로드:

`josm --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- JOSM을 시작하고 특정 경계 상자를 원시 GPS로 다운로드:

`josm --downloadgps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- 플러그인 없이 JOSM 시작:

`josm --skip-plugins`
