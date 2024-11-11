---
layout: page
title: linux/smbpasswd (한국어)
description: "Samba 사용자 추가/제거 또는 비밀번호 변경."
content_hash: 84189860bfc40df88cc6247681410587f757fc92
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/smbpasswd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/smbpasswd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># smbpasswd

Samba 사용자 추가/제거 또는 비밀번호 변경.
Samba 사용자는 기존의 로컬 유닉스 계정이 있어야 합니다.
더 많은 정보: <https://manned.org/smbpasswd.8>.

- 현재 사용자의 SMB 비밀번호 변경:

`smbpasswd`

- 지정된 사용자를 Samba에 추가하고 비밀번호 설정 (사용자는 시스템에 이미 존재해야 함):

`sudo smbpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 기존 Samba 사용자의 비밀번호 수정:

`sudo smbpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- Samba 사용자 삭제 (유닉스 계정이 삭제된 경우에는 `pdbedit` 사용):

`sudo smbpasswd -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
