---
layout: page
title: windows/takeown (한국어)
description: "파일 또는 디렉토리의 소유권을 가져옵니다."
content_hash: 92b843ba00c7161c33c92d492cdf5f40bee0d082
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/takeown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/takeown.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/takeown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># takeown

파일 또는 디렉토리의 소유권을 가져옵니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- 지정된 파일의 소유권을 취득:

`takeown /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 지정된 디렉토리의 소유권을 취득:

`takeown /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 지정된 디렉토리 및 모든 하위 디렉토리의 소유권을 취득:

`takeown /r /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 현재 사용자 대신 관리자 그룹의 소유권으로 변경:

`takeown /a /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>
