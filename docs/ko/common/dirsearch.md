---
layout: page
title: common/dirsearch (한국어)
description: "웹 경로 스캐너."
content_hash: 7a1d450d28bf110f65935f29afb2c133b4ff596e
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dirsearch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirsearch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirsearch

웹 경로 스캐너.
더 많은 정보: <https://github.com/maurosoria/dirsearch>.

- 공통 확장자를 가진 공통 경로를 웹 서버에서 검색:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list`

- `.php` 확장자를 사용하여 일반 경로에 대한 웹 서버 목록을 스캔:

`dirsearch --url-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url-list.txt</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>

- 공통 확장자를 사용하여 사용자 정의 경로를 웹 서버에서 검색:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url-paths.txt</span>

- 쿠키를 사용하여 웹 서버를 검색:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --cookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿠키</span>

- `HEAD` HTTP 메소드를 사용하여 웹 서버를 스캔:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --http-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 웹 서버를 스캔하고, 결과를 `.json` 파일에 저장:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --json-report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/리포트.json</span>
