---
layout: page
title: linux/archlinux-java (한국어)
description: "설치된 자바 환경 간 전환."
content_hash: d154ab5185858ffda78a2132ab2ccc16e1bc090b
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/archlinux-java.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/archlinux-java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/archlinux-java.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/archlinux-java.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># archlinux-java

설치된 자바 환경 간 전환.
더 많은 정보: <https://wiki.archlinux.org/title/Java#Switching_between_JVM>.

- 설치된 자바 환경 목록 나열:

`archlinux-java status`

- 현재 기본 자바 환경의 짧은 이름 반환:

`archlinux-java get`

- 기본 자바 환경 설정:

`archlinux-java set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자바_환경</span>

- 기본 자바 환경 설정 해제:

`archlinux-java unset`

- 잘못되었거나 손상된 기본 자바 환경 구성 수정:

`archlinux-java fix`
