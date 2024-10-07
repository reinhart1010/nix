---
layout: page
title: common/git-utimes (한국어)
description: "파일의 수정 시간을 마지막 커밋 날짜로 변경. 작업 트리 또는 색인에 있는 파일은 건드리지 않습니다."
content_hash: 7c3bfa1dacc3de43e49bed4d04100ec3b5d48b3a
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-utimes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-utimes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git utimes

파일의 수정 시간을 마지막 커밋 날짜로 변경. 작업 트리 또는 색인에 있는 파일은 건드리지 않습니다.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>.

- 모든 파일의 수정 시간을 마지막 커밋 날짜로 변경:

`git utimes`

- 마지막 커밋 날짜보다 최신인 파일의 수정 시간을 변경하고, 로컬 리포지토리에서 커밋된 파일의 원래 수정 시간을 유지:

`git utimes --newer`
