---
layout: page
title: freebsd/df (한국어)
description: "파일 시스템 디스크 공간 사용량 개요를 표시합니다."
content_hash: 0c625289e27af6d21f01d5e7746152f94e0f8c2c
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/freebsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/df.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

파일 시스템 디스크 공간 사용량 개요를 표시합니다.
더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?df>.

- 512바이트 단위로 모든 파일 시스템과 디스크 사용량 표시:

`df`

- [h]uman-readable(1024의 거듭제곱에 기반한) 단위를 사용해 총합 표시:

`df -h -c`

- [H]uman-readable(1000의 거듭제곱에 기반한) 단위 사용:

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- 주어진 파일 또는 디렉토리를 포함하는 파일 시스템 및 디스크 사용량 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- [i]노드의 수 및 사용된 노드 수를 포함해 파일 시스템 [T]ypes에 대한 통계 포함:

`df -iT`

- 공간 값을 쓸 때 1024바이트 단위 사용하기:

`df -k`

- [P]ortable한 방식으로 정보 표시:

`df -P`
