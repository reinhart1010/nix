---
layout: page
title: common/git-checkout-index (한국어)
description: "색인에서 작업 트리로 파일 복사."
content_hash: f400718e3b5a3c2bb82afcd378c55938bc2c5bea
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-checkout-index.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout-index.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout-index.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-checkout-index.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git checkout-index

색인에서 작업 트리로 파일 복사.
더 많은 정보: <https://git-scm.com/docs/git-checkout-index>.

- 마지막 커밋 이후 삭제된 파일 복원:

`git checkout-index --all`

- 마지막 커밋 이후 삭제되거나 변경된 파일 복원:

`git checkout-index --all --force`

- 마지막 커밋 이후 변경된 파일 복원, 삭제된 파일은 무시:

`git checkout-index --all --force --no-create`

- 마지막 커밋 시점의 전체 트리 복사본을 지정된 디렉토리에 내보내기 (끝의 슬래시가 중요):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/내보내기_폴더/</span>
