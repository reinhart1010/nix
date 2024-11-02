---
layout: page
title: windows/out-string (한국어)
description: "입력 객체를 문자열로 출력합니다."
content_hash: 2a87ff5431f2e0e139d23f82c17a787d7da5307f
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/out-string.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/out-string.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Out-String

입력 객체를 문자열로 출력합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- 호스트 정보를 문자열로 출력:

`Get-Alias | Out-String`

- 모든 객체를 단일 문자열로 연결하는 대신 각 객체를 문자열로 변환:

`Get-Alias | Out-String -Stream`

- `Width` 매개변수를 사용하여 잘림을 방지:

`@{TestKey = ('x' * 200)} | Out-String -Width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">250</span>
