---
layout: page
title: common/rr (한국어)
description: "프로그램 실행을 기록하고 재생하기 위한 디버깅 도구."
content_hash: edcfff6932cd79efbbda1120fbc5e1f320a5e954
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rr

프로그램 실행을 기록하고 재생하기 위한 디버깅 도구.
더 많은 정보: <https://rr-project.org/>.

- 애플리케이션 기록:

`rr record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리 --arg1 --arg2</span>

- 마지막으로 기록된 실행 재생:

`rr replay`
