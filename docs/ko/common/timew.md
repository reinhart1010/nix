---
layout: page
title: common/timew (한국어)
description: "활동의 지속 시간을 측정하는 시간 추적 도구."
content_hash: 70aaeb46a0a4a189b38b9675bba71624e1fe1f96
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/timew.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/timew.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># timew

활동의 지속 시간을 측정하는 시간 추적 도구.
더 많은 정보: <https://timewarrior.net/docs>.

- 추적할 활동에 태그 이름을 부여하여 새 스톱워치 시작:

`timew start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">활동_태그</span>

- 실행 중인 스톱워치 보기:

`timew`

- 주어진 태그 이름으로 스톱워치 중지:

`timew stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">활동_태그</span>

- 실행 중인 모든 스톱워치 중지:

`timew stop`

- 추적된 항목 보기:

`timew summary`
