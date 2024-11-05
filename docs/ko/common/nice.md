---
layout: page
title: common/nice (한국어)
description: "프로그램을 사용자 정의 스케줄링 우선순위(친화도)로 실행."
content_hash: f3c0ff249173a81b014037246e4aa799ee9318ec
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nice

프로그램을 사용자 정의 스케줄링 우선순위(친화도)로 실행.
친화도 값은 -20(가장 높은 우선순위)에서 19(가장 낮은 우선순위)까지 범위.
더 많은 정보: <https://www.gnu.org/software/coreutils/nice>.

- 변경된 우선순위로 프로그램 실행:

`nice -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">친화도_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명시적 옵션으로 우선순위 정의:

`nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--adjustment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">친화도_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
