---
layout: page
title: common/git-unlock (한국어)
description: "Git 저장소에서 특정 파일의 잠금을 해제하여 커밋으로 수정할 수 있도록 합니다."
content_hash: 79dc34632820f4f0df48978e537fce53684a5467
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-unlock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-unlock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git unlock

Git 저장소에서 특정 파일의 잠금을 해제하여 커밋으로 수정할 수 있도록 합니다.
`git-extras`의 일부입니다. 같이 보기: `git lock`.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-unlock>.

- 이전에 잠긴 로컬 파일의 변경 사항을 커밋할 수 있도록 설정:

`git unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
