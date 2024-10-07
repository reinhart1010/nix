---
layout: page
title: common/git-lfs (한국어)
description: "Git 저장소에서 대용량 파일을 다루기 위한 도구."
content_hash: 15ca30a3a2938bf2888bbd06a32639ce72140755
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-lfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-lfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-lfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-lfs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-lfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-lfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git lfs

Git 저장소에서 대용량 파일을 다루기 위한 도구.
더 많은 정보: <https://git-lfs.com>.

- Git LFS 초기화:

`git lfs install`

- 특정 패턴의 파일 추적:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Git LFS 엔드포인트 URL 변경 (LFS 서버가 Git 서버와 분리된 경우 유용):

`git config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--file</span>` .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_endpoint_url</span>

- 추적된 패턴 나열:

`git lfs track`

- 커밋된 추적 파일 나열:

`git lfs ls-files`

- 모든 Git LFS 객체를 원격 서버에 푸시 (오류 발생 시 유용):

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- 모든 Git LFS 객체 가져오기:

`git lfs fetch`

- 모든 Git LFS 객체 체크아웃:

`git lfs checkout`
