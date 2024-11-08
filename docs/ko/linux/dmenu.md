---
layout: page
title: linux/dmenu (한국어)
description: "동적 메뉴."
content_hash: 65e5b4d6af23cf3deac14d19bc607a4f9249784f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dmenu.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmenu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dmenu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmenu

동적 메뉴.
각 항목이 새 줄에 있는 텍스트 입력에서 메뉴 생성.
더 많은 정보: <https://manned.org/dmenu>.

- `ls` 명령어의 출력을 메뉴로 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | dmenu`

- 새 줄(`\n`)로 구분된 사용자 정의 항목으로 메뉴 표시:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu`

- 여러 항목 중 사용자가 선택한 항목을 파일에 저장:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- 특정 모니터에서 dmenu 실행:

`ls | dmenu -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 화면 아래쪽에 dmenu 표시:

`ls | dmenu -b`
