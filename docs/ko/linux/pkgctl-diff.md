---
layout: page
title: linux/pkgctl-diff (한국어)
description: "패키지 파일을 다양한 모드로 비교."
content_hash: b27af97f77b3ac31b4fe7689027808fbcf8f57dd
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkgctl-diff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pkgctl-diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkgctl-diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgctl diff

패키지 파일을 다양한 모드로 비교.
같이 보기: `pkgctl`.
더 많은 정보: <https://manned.org/pkgctl-diff.1>.

- tar 콘텐츠 [l]리스트 비교 모드(기본값)로 패키지 파일 비교:

`pkgctl diff --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일|패키지명</span>

- [d]iffoscope 비교 모드로 패키지 파일 비교:

`pkgctl diff --diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일|패키지명</span>

- `.PKGINFO` 비교 모드로 패키지 파일 비교:

`pkgctl diff --pkginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일|패키지명</span>

- `.BUILDINFO` 비교 모드로 패키지 파일 비교:

`pkgctl diff --buildinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일|패키지명</span>
