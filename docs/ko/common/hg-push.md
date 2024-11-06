---
layout: page
title: common/hg-push (한국어)
description: "로컬 저장소의 변경 사항을 지정된 대상으로 푸시."
content_hash: f2bc175594c51a08b04afcbd3a9d55f0a7ffd168
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-push.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg push

로컬 저장소의 변경 사항을 지정된 대상으로 푸시.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#push>.

- "기본" 원격 경로로 변경 사항 푸시:

`hg push`

- 지정된 원격 저장소로 변경 사항 푸시:

`hg push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 존재하지 않는 경우 새 브랜치 푸시 (기본적으로 비활성화됨):

`hg push --new-branch`

- 특정 리비전 체인지셋을 지정하여 푸시:

`hg push --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

- 특정 브랜치를 지정하여 푸시:

`hg push --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>

- 특정 북마크를 지정하여 푸시:

`hg push --bookmark `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크</span>
