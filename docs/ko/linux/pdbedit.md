---
layout: page
title: linux/pdbedit (한국어)
description: "Samba 사용자 데이터베이스 편집."
content_hash: 0f5b0b72a9f8c0e681dc2426acf4ef6fe9b0f11c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pdbedit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pdbedit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdbedit

Samba 사용자 데이터베이스 편집.
간단한 사용자 추가/제거/비밀번호 변경은 `smbpasswd`를 사용할 수도 있습니다.
더 많은 정보: <https://manned.org/pdbedit>.

- 모든 Samba 사용자 나열 (설정을 보려면 자세히 플래그 사용):

`sudo pdbedit --list --verbose`

- 기존 Unix 사용자를 Samba에 추가 (비밀번호 입력 요청):

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --create`

- Samba 사용자 제거:

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --delete`

- Samba 사용자의 실패한 비밀번호 시도 횟수 초기화:

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --bad-password-count-reset`
