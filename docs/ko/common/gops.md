---
layout: page
title: common/gops (한국어)
description: "현재 시스템에서 실행중인 Go 프로세스를 나열하고 진단."
content_hash: 0f360cceaf8504c3daa7bfa4ced408a3f56ecd42
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/gops.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gops.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gops

현재 시스템에서 실행중인 Go 프로세스를 나열하고 진단.
더 많은 정보: <https://github.com/google/gops>.

- 로컬에서 실행되는 모든 go 프로세스를 출력:

`gops`

- 프로세스에 대한 추가 정보를 출력:

`gops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스아이디</span>

- 프로세스 트리 출력:

`gops tree`

- 대상 프로그램에서 현재 스택 추적 현황을 출력:

`gops stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스아이디|주소</span>

- 현재 런타임 메모리 통계를 출력:

`gops memstats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스아이디|주소</span>
