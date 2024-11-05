---
layout: page
title: common/xephyr (한국어)
description: "X 애플리케이션으로 실행되는 중첩 X 서버."
content_hash: 7cf5f3748b241c9749eca6aa24efe8cbc3747d6b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xephyr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xephyr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Xephyr

X 애플리케이션으로 실행되는 중첩 X 서버.
더 많은 정보: <https://manned.org/xserver-xephyr>.

- 디스플레이 ID ":2"로 검은색 창 생성:

`Xephyr -br -ac -noreset -screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:2</span>

- 새 화면에서 X 애플리케이션 시작:

`DISPLAY=:2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_이름</span>
