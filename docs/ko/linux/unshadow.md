---
layout: page
title: linux/unshadow (한국어)
description: "시스템이 섀도우 비밀번호를 사용하는 경우 전통적인 유닉스 비밀번호 파일을 얻기 위해 John the Ripper 프로젝트에서 제공하는 유틸리티."
content_hash: ada5d9e37bf18f96f540ea2826b31bc964a61003
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/unshadow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/unshadow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unshadow

시스템이 섀도우 비밀번호를 사용하는 경우 전통적인 유닉스 비밀번호 파일을 얻기 위해 John the Ripper 프로젝트에서 제공하는 유틸리티.
더 많은 정보: <https://www.openwall.com/john/>.

- 현재 시스템의 `/etc/shadow`와 `/etc/passwd` 결합:

`sudo unshadow /etc/passwd /etc/shadow`

- 임의의 섀도우 및 비밀번호 [f]파일 결합:

`sudo unshadow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/passwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/shadow</span>
