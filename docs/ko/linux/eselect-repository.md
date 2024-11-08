---
layout: page
title: linux/eselect-repository (한국어)
description: "Portage를 위한 ebuild 저장소를 구성하는 `eselect` 모듈."
content_hash: 80875ab15922768b649528a3ba37e4f545c21b19
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/eselect-repository.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/eselect-repository.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/eselect-repository.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-repository.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect repository

Portage를 위한 ebuild 저장소를 구성하는 `eselect` 모듈.
저장소를 활성화한 후에는 `emerge --sync repo_name`을 실행하여 ebuild를 다운로드해야 합니다.
더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- <https://repos.gentoo.org>에 등록된 모든 ebuild 저장소 나열:

`eselect repository list`

- 활성화된 저장소 나열:

`eselect repository list -i`

- `list` 명령에서 이름이나 색인으로 저장소 활성화:

`eselect repository enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|색인</span>

- 등록되지 않은 저장소 활성화:

`eselect repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync|git|mercurial|svn|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">동기화_URI</span>

- 저장소의 내용을 제거하지 않고 비활성화:

`eselect repository disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소1 저장소2 ...</span>

- 저장소를 비활성화하고 내용을 제거:

`eselect repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소1 저장소2 ...</span>

- 로컬 저장소를 생성하고 활성화:

`eselect repository create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>
