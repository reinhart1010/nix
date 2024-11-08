---
layout: page
title: linux/dconf (한국어)
description: "dconf 데이터베이스 관리."
content_hash: 8e572e563b45861f5ec9406cac18bfd0c08ef367
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dconf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dconf

dconf 데이터베이스 관리.
같이 보기: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`.
더 많은 정보: <https://manned.org/dconf>.

- 특정 키 값을 출력:

`dconf read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>

- 특정 경로의 하위 디렉토리 및 하위 키를 출력:

`dconf list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/폴더/</span>

- 특정 키 값 쓰기:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 특정 키 값 초기화:

`dconf reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>

- 특정 키/디렉토리의 변경 사항 감시:

`dconf watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키|/경로/대상/폴더/</span>

- 특정 디렉토리를 INI 파일 형식으로 덤프:

`dconf dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/폴더/</span>
