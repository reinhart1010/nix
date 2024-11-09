---
layout: page
title: common/smartctl (한국어)
description: "디스크 상태를 SMART 데이터를 통해 모니터링."
content_hash: ea5659d741a55af8c2cab64001c0d2e3e2dfcb0e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/smartctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/smartctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># smartctl

디스크 상태를 SMART 데이터를 통해 모니터링.
더 많은 정보: <https://www.smartmontools.org>.

- SMART 건강 요약 표시:

`sudo smartctl --health `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 장치 정보 표시:

`sudo smartctl --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 백그라운드에서 짧은 자체 테스트 시작:

`sudo smartctl --test short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 현재/마지막 자체 테스트 상태 및 기타 SMART 기능 표시:

`sudo smartctl --capabilities `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 포괄적인 SMART 데이터 표시:

`sudo smartctl --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
