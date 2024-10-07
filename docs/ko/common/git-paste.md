---
layout: page
title: common/git-paste (한국어)
description: "`pastebinit`을 사용하여 커밋을 pastebin 사이트에 전송."
content_hash: ac3221dfe443ae618b8bee5c28239a83c74b3229
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-paste.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-paste.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git paste

`pastebinit`을 사용하여 커밋을 pastebin 사이트에 전송.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>.

- 현재 브랜치와 업스트림 간의 패치를 `pastebinit`을 사용하여 pastebin에 전송:

`git paste`

- `git format-patch`에 옵션을 전달하여 다른 커밋 집합을 선택 ( `@^`는 HEAD의 부모를 선택하여 현재 체크아웃된 커밋을 전송):

`git paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@^</span>
