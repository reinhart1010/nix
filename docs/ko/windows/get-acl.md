---
layout: page
title: windows/get-acl (한국어)
description: "파일이나 레지스트리 키와 같은 리소스의 보안 설명자를 가져옵니다."
content_hash: 81bc9757e15fc71be5445ef06b2b6e0a5c3c4127
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-acl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-acl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-Acl

파일이나 레지스트리 키와 같은 리소스의 보안 설명자를 가져옵니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- 특정 디렉토리의 ACL 표시:

`Get-Acl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 레지스트리 키의 ACL 가져오기:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HKLM:\System\CurrentControlSet\Control</span>` | Format-List`
