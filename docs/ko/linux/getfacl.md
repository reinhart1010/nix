---
layout: page
title: linux/getfacl (한국어)
description: "파일 접근 제어 목록(ACL) 가져오기."
content_hash: 481c2ecf90ccdf65876903e35ad5fe56379fdcb4
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/getfacl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/getfacl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># getfacl

파일 접근 제어 목록(ACL) 가져오기.
더 많은 정보: <https://manned.org/getfacl>.

- 파일 접근 제어 목록 표시:

`getfacl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 사용자 및 그룹 ID를 [n]숫자로 표시하여 파일 접근 제어 목록 표시:

`getfacl --numeric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- [t]표 형식으로 파일 접근 제어 목록 표시:

`getfacl --tabular `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
