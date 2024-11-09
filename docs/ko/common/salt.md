---
layout: page
title: common/salt (한국어)
description: "원격 salt 미니언에서 명령을 실행하고 상태를 확인."
content_hash: 6fd4c3fedfddc6c044f551cce9cb6cec748b8107
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/salt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/salt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># salt

원격 salt 미니언에서 명령을 실행하고 상태를 확인.
더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/index.html>.

- 연결된 미니언 나열:

`salt '*' test.ping`

- 모든 연결된 미니언에서 highstate 실행:

`salt '*' state.highstate`

- 일부 미니언에서 OS 패키지 관리자(apt, yum, brew)를 사용하여 패키지 업그레이드:

`salt '*.example.com' pkg.upgrade`

- 특정 미니언에서 임의의 명령 실행:

`salt '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미니언_ID</span>`' cmd.run "ls "`
