---
layout: page
title: windows/sdelete (한국어)
description: "디스크에서 파일/디렉토리를 안전하게 삭제하거나 볼륨/물리적 디스크의 사용 가능한 공간을 정리합니다."
content_hash: abf0a178ac62161c6cea36a3be9c632c98e14e7b
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/windows/sdelete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/sdelete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/sdelete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdelete

디스크에서 파일/디렉토리를 안전하게 삭제하거나 볼륨/물리적 디스크의 사용 가능한 공간을 정리합니다.
더 많은 정보: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- 3회 덮어쓰기로 파일 삭제:

`sdelete -p 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1 경로\대상\파일2 ...</span>

- 폴더와 하위 디렉토리를 1회 덮어쓰기로 삭제:

`sdelete -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더1 경로\대상\폴더2 ...</span>

- 볼륨 D의 사용 가능한 공간을 3회 덮어쓰기로 정리:

`sdelete -p 3 D:`

- 물리적 디스크 2의 사용 가능한 공간을 0으로 정리 (볼륨이 포함되지 않아야 함):

`sdelete -z 2`
