---
layout: page
title: common/svn (한국어)
description: "Subversion 명령줄 클라이언트 도구."
content_hash: 921515fe46f7fbdfa8dbac27807acb92caf51d4a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/svn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/svn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svn

Subversion 명령줄 클라이언트 도구.
더 많은 정보: <https://subversion.apache.org>.

- 저장소에서 작업 복사본 체크아웃:

`svn co `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/URL</span>

- 저장소의 변경 사항을 작업 복사본에 반영:

`svn up`

- 파일 및 디렉토리를 버전 관리에 추가하여 저장소에 추가될 준비. 다음 커밋에 추가됨:

`svn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>

- 작업 복사본의 변경 사항을 저장소에 전송:

`svn ci -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_로그_메시지</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>`]`

- 마지막 10개 리비전의 변경 사항을 표시하고 각 리비전에 수정된 파일 표시:

`svn log -vl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 도움말 표시:

`svn help`
