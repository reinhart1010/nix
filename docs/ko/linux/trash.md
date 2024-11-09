---
layout: page
title: linux/trash (한국어)
description: "휴지통/재활용통 관리."
content_hash: d225a3fd7f81f45dd18edd3c1eee0342cda319cd
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/trash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/trash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/trash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/trash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trash

휴지통/재활용통 관리.
더 많은 정보: <https://github.com/andreafrancia/trash-cli>.

- 파일을 휴지통으로 보내기:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 휴지통에 있는 모든 파일 나열:

`trash-list`

- 휴지통에서 파일을 상호작용하며 복원:

`trash-restore`

- 휴지통 비우기:

`trash-empty`

- 휴지통에서 10일 이상 된 모든 파일을 영구 삭제:

`trash-empty 10`

- 특정 블롭 패턴과 일치하는 휴지통의 모든 파일 제거:

`trash-rm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.o</span>`"`

- 특정 원래 위치의 모든 파일 제거:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일_또는_폴더</span>
