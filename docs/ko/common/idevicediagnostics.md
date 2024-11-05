---
layout: page
title: common/idevicediagnostics (한국어)
description: "iOS 장치의 진단 인터페이스와 상호 작용."
content_hash: 703c57bb0cbad13d88c3c587dc02fae55b3881d8
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/idevicediagnostics.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/idevicediagnostics.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># idevicediagnostics

iOS 장치의 진단 인터페이스와 상호 작용.
더 많은 정보: <https://manned.org/idevicediagnostics>.

- 진단 정보를 출력:

`idevicediagnostics diagnostics`

- Print mobilegestalt 키 값 출력:

`idevicediagnostics mobilegestalt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키2</span>

- 장치 종료, 다시 시작 또는 절전 모드:

`idevicediagnostics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shutdown|restart|sleep</span>
