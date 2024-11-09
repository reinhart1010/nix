---
layout: page
title: linux/mountpoint (한국어)
description: "디렉토리가 파일 시스템 마운트 지점인지 확인합니다."
content_hash: 86cb2bb2ecab96ed70ab3c269c7aa547f2ba71cc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mountpoint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mountpoint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mountpoint

디렉토리가 파일 시스템 마운트 지점인지 확인합니다.
더 많은 정보: <https://manned.org/mountpoint>.

- 디렉토리가 마운트 지점인지 확인:

`mountpoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 출력 없이 디렉토리가 마운트 지점인지 확인:

`mountpoint -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 마운트 지점의 파일 시스템 주요/부 번호 표시:

`mountpoint --fs-devno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
