---
layout: page
title: linux/rmdir (한국어)
description: "파일이 없는 디렉토리를 제거합니다."
content_hash: 3373b5f4f8309712f043d32137106f67af2f7be8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rmdir.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rmdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rmdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmdir

파일이 없는 디렉토리를 제거합니다.
같이 보기: `rm`.
더 많은 정보: <https://www.gnu.org/software/coreutils/rmdir>.

- 특정 디렉토리 제거:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 특정 중첩 디렉토리를 재귀적으로 제거:

`rmdir --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>
