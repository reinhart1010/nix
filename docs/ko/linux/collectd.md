---
layout: page
title: linux/collectd (한국어)
description: "시스템 통계 수집 데몬."
content_hash: 1f0f8cd2591bee5ab2283894ae0261273a181d56
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/collectd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/collectd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># collectd

시스템 통계 수집 데몬.
더 많은 정보: <https://collectd.org/>.

- 구성 파일을 테스트하고 종료:

`collectd -t`

- 플러그인 데이터 수집 기능을 테스트하고 종료:

`collectd -T`

- `collectd` 시작:

`collectd`

- 사용자 지정 구성 파일 위치 지정:

`collectd -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 지정 PID 파일 위치 지정:

`collectd -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 백그라운드로 포크하지 않음:

`collectd -f`

- 도움말 및 버전 표시:

`collectd -h`
