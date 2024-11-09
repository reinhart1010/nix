---
layout: page
title: common/timetrap (한국어)
description: "Ruby로 작성된 간단한 명령줄 시간 추적기."
content_hash: d516a05d53949e75ac7f54d5ff83c20090e8cf29
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/timetrap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/timetrap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># timetrap

Ruby로 작성된 간단한 명령줄 시간 추적기.
더 많은 정보: <https://github.com/samg/timetrap>.

- 새 타임시트 생성:

`timetrap sheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임시트</span>

- 5분 전에 시작된 항목 체크인:

`timetrap in --at "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5분 전</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_노트</span>

- 현재 타임시트 표시:

`timetrap display`

- 마지막 항목의 종료 시간 수정:

`timetrap edit --end `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>
