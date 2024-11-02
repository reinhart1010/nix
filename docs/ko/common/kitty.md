---
layout: page
title: common/kitty (한국어)
description: "빠르고 기능이 풍부한 GPU 기반 터미널 에뮬레이터."
content_hash: 6e5f7900deb1ff1de5997b92400149431b009077
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/kitty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kitty.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kitty.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kitty

빠르고 기능이 풍부한 GPU 기반 터미널 에뮬레이터.
더 많은 정보: <https://sw.kovidgoyal.net/kitty/>.

- 새로운 터미널 열기:

`kitty`

- 지정된 제목으로 창 열기:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`"`

- 테마 선택기 내장 기능 시작:

`kitty +kitten themes`

- 터미널에 이미지 표시:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- `stdin`의 내용을 클립보드에 복사:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제</span>` | kitty +kitten clipboard`
