---
layout: page
title: common/xzless (한국어)
description: "`xz` 및 `lzma` 압축 파일에서 텍스트를 표시."
content_hash: 4011280fbdbe213c84dd00d9b5c1ae65f656e145
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xzless.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzless.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzless.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzless

`xz` 및 `lzma` 압축 파일에서 텍스트를 표시.
같이 보기: `less`.
더 많은 정보: <https://manned.org/xzless>.

- 압축 파일 보기:

`xzless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일을 보고 줄 번호 표시:

`xzless --LINE-NUMBERS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일을 보고 첫 화면에 전체 파일이 표시될 수 있으면 종료:

`xzless --quit-if-one-screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
