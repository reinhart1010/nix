---
layout: page
title: common/mkdir (한국어)
description: "디렉토리를 생성하고 해당 권한을 설정합니다."
content_hash: 5c359d57aad6e57382c863c849016ee0e12616c7
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/mkdir.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mkdir.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mkdir.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mkdir.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mkdir.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mkdir.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/mkdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mkdir.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/mkdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mkdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mkdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mkdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkdir

디렉토리를 생성하고 해당 권한을 설정합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/mkdir>.

- 특정 디렉토리 생성:

`mkdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 필요시 특정 디렉토리와 그 [상위] 디렉토리를 생성:

`mkdir -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 특정 권한으로 디렉토리 생성:

`mkdir -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rwxrw-r--</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>
