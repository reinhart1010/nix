---
layout: page
title: linux/fallocate (한국어)
description: "파일에 디스크 공간을 예약하거나 할당 해제."
content_hash: 04c87d6df644f3c42d8c66c930eb074db7d01eb8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fallocate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fallocate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fallocate

파일에 디스크 공간을 예약하거나 할당 해제.
이 도구는 공간을 할당할 때 0으로 초기화하지 않습니다.
더 많은 정보: <https://manned.org/fallocate>.

- 700 MiB의 디스크 공간을 차지하는 파일 예약:

`fallocate --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">700M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미 할당된 파일을 200 MiB 줄이기:

`fallocate --collapse-range --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 100 MiB 이후의 20 MB 공간 줄이기:

`fallocate --collapse-range --offset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100M</span>` --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
