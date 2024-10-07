---
layout: page
title: common/git-obliterate (한국어)
description: "Git 저장소에서 파일을 삭제하고 해당 기록을 지웁니다."
content_hash: 5a15565706310df3c18ba1086f25f722981d4cf0
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-obliterate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-obliterate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git obliterate

Git 저장소에서 파일을 삭제하고 해당 기록을 지웁니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- 특정 파일의 존재를 지우기:

`git obliterate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름_1 파일_이름_2 ...</span>

- 두 커밋 사이의 특정 파일 존재를 지우기:

`git obliterate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름_1 파일_이름_2 ...</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시_2</span>
