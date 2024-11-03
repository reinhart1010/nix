---
layout: page
title: windows/get-filehash (한국어)
description: "파일의 해시를 계산."
content_hash: 7541134338d16f33439a436fa3414b1b06514f82
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-filehash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/get-filehash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-filehash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-FileHash

파일의 해시를 계산.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- SHA256 알고리즘을 사용하여 지정된 파일의 해시 계산:

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 지정된 알고리즘을 사용하여 지정된 파일의 해시 계산:

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -Algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SHA1|SHA384|SHA256|SHA512|MD5</span>
