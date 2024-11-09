---
layout: page
title: linux/mkisofs (한국어)
description: "디렉터리에서 ISO 파일 생성."
content_hash: 597f7be2b9127ace68eec7d2024160e195dad31a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mkisofs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkisofs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkisofs

디렉터리에서 ISO 파일 생성.
`genisoimage`라는 별칭으로도 사용됩니다.
더 많은 정보: <https://manned.org/mkisofs>.

- 디렉터리에서 ISO 생성:

`mkisofs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_디렉터리</span>

- ISO 생성 시 디스크 레이블 설정:

`mkisofs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.iso</span>` -V "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블_이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_디렉터리</span>
