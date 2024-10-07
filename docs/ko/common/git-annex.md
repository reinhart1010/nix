---
layout: page
title: common/git-annex (한국어)
description: "Git을 사용하여 파일을 관리하지만, 파일의 내용을 체크인하지 않습니다."
content_hash: 16f1bcbaaf909bf65893e917026c552e0d9eb6fe
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-annex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git annex

Git을 사용하여 파일을 관리하지만, 파일의 내용을 체크인하지 않습니다.
파일이 annexed되면, 해당 내용이 키-값 저장소로 이동되고, 내용을 가리키는 심볼릭 링크가 생성됩니다.
더 많은 정보: <https://git-annex.branchable.com>.

- Git annex로 저장소 초기화:

`git annex init`

- 파일 추가:

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일 또는 디렉토리의 현재 상태 표시:

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 로컬 저장소를 원격과 동기화:

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격</span>

- 파일 또는 디렉토리 가져오기:

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 도움말 표시:

`git annex help`
