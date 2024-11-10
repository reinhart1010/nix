---
layout: page
title: linux/xfce4-terminal (한국어)
description: "XFCE4 터미널 에뮬레이터."
content_hash: 8d8c096e913264d43597e7a4f5126df0d5ce7ddf
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xfce4-terminal.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/xfce4-terminal.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xfce4-terminal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xfce4-terminal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xfce4-terminal

XFCE4 터미널 에뮬레이터.
더 많은 정보: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- 새 터미널 창 열기:

`xfce4-terminal`

- 초기 제목 설정:

`xfce4-terminal --initial-title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초기_제목</span>`"`

- 현재 터미널 창에 새 탭 열기:

`xfce4-terminal --tab`

- 새 터미널 창에서 명령어 실행:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_및_인수</span>`"`

- 실행한 명령어가 완료된 후에도 터미널 유지:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_및_인수</span>`" --hold`

- 여러 새 탭을 열고 각 탭에서 명령어 실행:

`xfce4-terminal --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1</span>`" --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어2</span>`"`
