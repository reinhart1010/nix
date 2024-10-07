---
layout: page
title: common/git-update-ref (한국어)
description: "Git 참조를 생성, 업데이트 및 삭제하는 Git 명령어."
content_hash: 015cc1904ce3ad8c64e6503ded38b7730287a801
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-update-ref.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-update-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-update-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-ref.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-update-ref.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git update-ref

Git 참조를 생성, 업데이트 및 삭제하는 Git 명령어.
더 많은 정보: <https://git-scm.com/docs/git-update-ref>.

- 참조 삭제 (첫 커밋을 소프트 리셋하는 데 유용):

`git update-ref -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 메시지와 함께 참조 업데이트:

`git update-ref -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4e95e05</span>
