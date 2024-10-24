---
layout: page
title: windows/rpcinfo (한국어)
description: "원격 컴퓨터에서 RPC를 통해 프로그램 목록 표시."
content_hash: d533b453df3930a2a1733708b5f2912fb26ed2cb
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/windows/rpcinfo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rpcinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/rpcinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpcinfo

원격 컴퓨터에서 RPC를 통해 프로그램 목록 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- 로컬 컴퓨터에 등록된 모든 프로그램 표시:

`rpcinfo`

- 원격 컴퓨터에 등록된 모든 프로그램 표시:

`rpcinfo /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터명</span>

- 원격 컴퓨터에서 특정 프로그램 호출:

`rpcinfo /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램명</span>

- 원격 컴퓨터에서 특정 프로그램 호출 (UDP 사용):

`rpcinfo /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램명</span>
