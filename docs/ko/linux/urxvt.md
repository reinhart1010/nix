---
layout: page
title: linux/urxvt (한국어)
description: "Rxvt-unicode."
content_hash: a21802e56b06b84455d78f4bdc2bb3557a525840
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/urxvt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urxvt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urxvt

Rxvt-unicode.
사용자 정의 가능한 터미널 에뮬레이터.
더 많은 정보: <https://manned.org/urxvt>.

- 새로운 urxvt 창 열기:

`urxvt`

- 특정 폴더에서 실행:

`urxvt -cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 새로운 urxvt 창에서 명령어 실행:

`urxvt -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령어 실행 후 창을 유지:

`urxvt --hold -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `sh` 셸 내에서 명령어 실행:

`urxvt -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
