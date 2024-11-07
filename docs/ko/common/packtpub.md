---
layout: page
title: common/packtpub (한국어)
description: "packtpub.com에서 무료로 제공되는 책을 다운로드."
content_hash: 36d72581f2aab327e65dee1af4ac51473ee134d5
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/packtpub.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/packtpub.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># packtpub

packtpub.com에서 무료로 제공되는 책을 다운로드.
더 많은 정보: <https://github.com/vladimyr/packtpub-cli>.

- 지정한 책 형식(기본값은 `pdf`)으로 오늘의 제공 책을 현재 디렉토리에 다운로드:

`packtpub download --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf|ebup|mobi</span>

- 오늘의 제공 책을 지정한 디렉토리에 다운로드:

`packtpub download --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- packtpub.com에 대한 대화형 로그인 시작:

`packtpub login`

- packtpub.com에서 로그아웃:

`packtpub logout`

- 오늘의 제공 정보 표시:

`packtpub view-offer`

- 기본 웹 브라우저에서 오늘의 제공 열기:

`packtpub view-offer`

- 현재 로그인된 사용자 표시:

`packtpub whoami`
