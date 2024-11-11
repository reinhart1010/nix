---
layout: page
title: linux/sshare (한국어)
description: "클러스터에 대한 연결의 공유 목록을 표시합니다."
content_hash: b8bb9f982979a77a0e2be84bfb0c34218a44244c
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sshare.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sshare.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sshare

클러스터에 대한 연결의 공유 목록을 표시합니다.
더 많은 정보: <https://slurm.schedmd.com/sshare.html>.

- Slurm 공유 정보 나열:

`sshare`

- 출력 형식 제어:

`sshare --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parsable|parsable2|json|yaml</span>

- 표시할 필드 제어:

`sshare --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식_문자열</span>

- 지정된 사용자에 대한 정보만 표시:

`sshare --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_ID_1,사용자_ID_2,...</span>
