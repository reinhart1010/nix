---
layout: page
title: linux/sherlock (한국어)
description: "소셜 네트워크에서 사용자명을 찾습니다."
content_hash: cca5dccdd5dbd107297540b433d2d7a9cbb7b7dd
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sherlock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sherlock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sherlock

소셜 네트워크에서 사용자명을 찾습니다.
더 많은 정보: <https://github.com/sherlock-project/sherlock>.

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 [f]파일에 저장:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 [f]폴더에 저장:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명1 사용자명2 ...</span>` --folderoutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- Tor 네트워크를 사용하여 소셜 네트워크에서 특정 사용자명 검색:

`sherlock --tor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 각 요청 후 새로운 Tor 회로로 요청 수행:

`sherlock --unique-tor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 프록시를 사용하여 소셜 네트워크에서 특정 사용자명 검색:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프록시_URL</span>

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 기본 웹 브라우저에서 열기:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --browse`

- 도움말 표시:

`sherlock --help`
