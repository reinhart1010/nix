---
layout: page
title: linux/smbget (한국어)
description: "SMB 서버에서 파일을 다운로드하기 위한 `wget` 유사 도구."
content_hash: b910fcde0a9a0e1535d2bd04096f27709a37440e
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/smbget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/smbget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># smbget

SMB 서버에서 파일을 다운로드하기 위한 `wget` 유사 도구.
더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- 서버에서 파일 다운로드:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>

- 공유 또는 폴더를 재귀적으로 다운로드:

`smbget --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share</span>

- 사용자명과 비밀번호로 연결:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명%비밀번호</span>

- 암호화된 전송 요구:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>` --encrypt`
