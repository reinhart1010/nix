---
layout: page
title: linux/powertop (한국어)
description: "배터리 전력 사용 최적화 도구."
content_hash: 2410fb2e17af9d16f4546db737db63c6fd80ba93
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/powertop.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/powertop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/powertop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># powertop

배터리 전력 사용 최적화 도구.
더 많은 정보: <https://github.com/fenrus75/powertop>.

- 전력 사용 측정 보정:

`sudo powertop --calibrate`

- 현재 디렉토리에 HTML 형식의 전력 사용 보고서 생성:

`sudo powertop --html=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전력_보고서.html</span>

- 최적 설정으로 조정:

`sudo powertop --auto-tune`

- 기본 20초 대신 지정한 초 동안의 보고서 생성:

`sudo powertop --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
