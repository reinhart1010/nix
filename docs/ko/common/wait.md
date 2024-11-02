---
layout: page
title: common/wait (한국어)
description: "프로세스가 완료될 때까지 대기."
content_hash: f68e25f5b5c2d372893c512a63df05da50bee96a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wait.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wait.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wait

프로세스가 완료될 때까지 대기.
더 많은 정보: <https://manned.org/wait>.

- 프로세스 ID (PID)를 사용하여 특정 프로세스가 종료될 때까지 대기하고 종료 상태 반환:

`wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 호출한 셸에서 알고 있는 모든 프로세스가 종료될 때까지 대기:

`wait`

- 작업이 완료될 때까지 대기:

`wait %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>
