---
layout: page
title: common/git-scp (한국어)
description: "현재 작업 트리에서 원격 저장소의 작업 디렉토리로 파일을 복사합니다."
content_hash: 88a620a42959773a7208373a2f7e7e5d9a677a1d
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-scp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-scp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git scp

현재 작업 트리에서 원격 저장소의 작업 디렉토리로 파일을 복사합니다.
`git-extras`의 일부입니다. 파일 전송에는 `rsync`를 사용합니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- 스테이지되지 않은 파일을 특정 원격으로 복사:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- 스테이지된 파일과 스테이지되지 않은 파일을 원격으로 복사:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` HEAD`

- 마지막 커밋에서 변경된 파일 및 모든 스테이지된 또는 스테이지되지 않은 파일을 원격으로 복사:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` HEAD~1`

- 특정 파일을 원격으로 복사:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 디렉토리를 원격으로 복사:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
