---
layout: page
title: common/git-repl (한국어)
description: "Git REPL (read-evaluate-print-loop) - 인터랙티브 Git 쉘."
content_hash: 23a9c28fdfc60e44c67070cc4f463769d60416de
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-repl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-repl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git repl

Git REPL (read-evaluate-print-loop) - 인터랙티브 Git 쉘.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-repl>.

- 인터랙티브 Git 쉘 시작:

`git repl`

- 인터랙티브 Git 쉘에서 Git 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_하위_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- 인터랙티브 Git 쉘에서 외부 (Git 이외의) 명령 실행:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- 인터랙티브 Git 쉘 종료 (또는 Ctrl + D 누르기):

`exit`
