---
layout: page
title: windows/choco-apikey (한국어)
description: "Chocolatey 소스의 API 키 관리."
content_hash: 9063dc606e141d1aa1c30fd2bfe70b50f1b87fbb
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-apikey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco apikey

Chocolatey 소스의 API 키 관리.
더 많은 정보: <https://chocolatey.org/docs/commands-apikey>.

- 소스 및 해당 API 키 목록 표시:

`choco apikey`

- 특정 소스 및 해당 API 키 표시:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_URL</span>`"`

- 소스에 대한 API 키 설정:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_URL</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">API_키</span>`"`

- 소스에 대한 API 키 제거:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_URL</span>`" --remove`
