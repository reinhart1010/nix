---
layout: page
title: windows/set-acl (한국어)
description: "지정된 항목(예: 파일 또는 레지스트리 키)의 보안 설명자를 변경합니다."
content_hash: 07ccd14dd086fe72cf1373475f33089b111606ef
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/set-acl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/set-acl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Set-Acl

지정된 항목(예: 파일 또는 레지스트리 키)의 보안 설명자를 변경합니다.
이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- 하나의 파일에서 보안 설명자를 복사하여 다른 파일에 적용:

`$OriginAcl = Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>`; Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -AclObject $OriginAcl`

- 파이프라인 연산자를 사용하여 설명자 전달:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` | Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>
