---
layout: page
title: common/git-check-attr (한국어)
description: "각 경로명에 대해 해당 경로명에 대한 gitattribute로 지정되지 않았는지, 설정되었는지 또는 해제되었는지 속성을 나열합니다."
content_hash: 74c915b59f5829aa438e767d315d8c8fd63f3dfb
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-check-attr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-check-attr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-attr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-check-attr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git check-attr

각 경로명에 대해 해당 경로명에 대한 gitattribute로 지정되지 않았는지, 설정되었는지 또는 해제되었는지 속성을 나열합니다.
더 많은 정보: <https://git-scm.com/docs/git-check-attr>.

- 파일의 모든 속성 값을 확인:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 특정 속성 값을 확인:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일들의 모든 속성 값을 확인:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 하나 이상의 파일에 대한 특정 속성 값을 확인:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
