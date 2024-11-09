---
layout: page
title: linux/waitpid (한국어)
description: "임의의 프로세스 종료를 대기."
content_hash: 45ef8538a4d8a4306d8f27ada0922e28f4577eb1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/waitpid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/waitpid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># waitpid

임의의 프로세스 종료를 대기.
같이 보기: `wait`.
더 많은 정보: <https://manned.org/waitpid.1>.

- 지정된 PID의 모든 프로세스가 종료될 때까지 대기:

`waitpid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- 최대 `n`초 동안 대기:

`waitpid --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- 지정된 PID가 이미 종료된 경우에도 오류 발생하지 않음:

`waitpid --exited `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- 지정된 프로세스 중 `n`개가 종료될 때까지 대기:

`waitpid --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- 도움말 표시:

`waitpid -h`
