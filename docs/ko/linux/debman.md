---
layout: page
title: linux/debman (한국어)
description: "설치되지 않은 패키지에서 매뉴얼 페이지를 읽습니다."
content_hash: efe4d38d729bce0317b7a680c185c90648a88380
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/debman.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debman.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debman

설치되지 않은 패키지에서 매뉴얼 페이지를 읽습니다.
더 많은 정보: <https://manned.org/debman.1>.

- 지정된 패키지가 제공하는 명령어에 대한 매뉴얼 페이지 읽기:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 다운로드할 패키지 버전 지정:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `.deb` 파일에서 매뉴얼 페이지 읽기:

`debman -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
