---
layout: page
title: common/git-coauthor (한국어)
description: "최신 커밋에 다른 작성자를 추가. 이 명령은 Git 기록을 다시 작성하므로, 다음 푸시 시 `--force`가 필요합니다."
content_hash: 7d8360f2361559de4dfd5e240afa651f2b5968c1
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-coauthor.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-coauthor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-coauthor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git coauthor

최신 커밋에 다른 작성자를 추가. 이 명령은 Git 기록을 다시 작성하므로, 다음 푸시 시 `--force`가 필요합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-coauthor>.

- 마지막 Git 커밋에 추가 작성자 삽입:

`git coauthor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name@example.com</span>
