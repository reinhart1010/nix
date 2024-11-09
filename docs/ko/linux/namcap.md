---
layout: page
title: linux/namcap (한국어)
description: "바이너리 패키지와 소스 `PKGBUILD`의 일반적인 패키징 실수를 검사합니다."
content_hash: 6a15e361ef3edcf7a89cadb091a7a39ba13b7f83
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/namcap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/namcap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># namcap

바이너리 패키지와 소스 `PKGBUILD`의 일반적인 패키징 실수를 검사합니다.
더 많은 정보: <https://manned.org/namcap.1>.

- 특정 `PKGBUILD` 파일 검사:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pkgbuild</span>

- 특정 패키지 파일 검사:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.pkg.tar.zst</span>

- 파일을 검사하고 추가 [i]정보 메시지 출력:

`namcap -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
