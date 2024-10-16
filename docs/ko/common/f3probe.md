---
layout: page
title: common/f3probe (한국어)
description: "위조 플래시 메모리가 있는지 블록 장치(예: 플래시 드라이브 또는 microSD 카드)를 조사."
content_hash: 4ce3db5afd7b7b0b4992171232a7c51d4ad2171e
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/f3probe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/f3probe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># f3probe

위조 플래시 메모리가 있는지 블록 장치(예: 플래시 드라이브 또는 microSD 카드)를 조사.
참고: `f3read`, `f3write`, `f3fix`.
더 많은 정보: <https://github.com/AltraMayor/f3>.

- 블록 장치 조사:

`sudo f3probe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/블록_장치</span>

- 가능한 최소한의 RAM을 사용:

`sudo f3probe --min-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/블록_장치</span>

- 디스크 작업에 걸리는 시간:

`sudo f3probe --time-ops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/블록_장치</span>
