---
layout: page
title: linux/xed (한국어)
description: "Cinnamon 데스크탑 환경에서 파일 편집."
content_hash: 5a40c22429191050524b1e8cf888e766c51f9078
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/xed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xed

Cinnamon 데스크탑 환경에서 파일 편집.
더 많은 정보: <https://github.com/linuxmint/xed>.

- 편집기 시작:

`xed`

- 특정 파일 열기:

`xed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 인코딩을 사용하여 파일 열기:

`xed --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WINDOWS-1252</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 지원되는 모든 인코딩 출력:

`xed --list-encodings`

- 특정 줄로 이동하여 파일 열기:

`xed +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
