---
layout: page
title: windows/show-markdown (한국어)
description: "VT100 이스케이프 시퀀스를 사용하거나 HTML을 사용하는 브라우저에서 친숙한 방법으로 콘솔의 Markdown 파일 또는 문자열을 표시합니다."
content_hash: e466238f8cdc7857ed5c34708fb792e190c13d63
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/show-markdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Show-Markdown

VT100 이스케이프 시퀀스를 사용하거나 HTML을 사용하는 브라우저에서 친숙한 방법으로 콘솔의 Markdown 파일 또는 문자열을 표시합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- 파일에서 콘솔로 Markdown 렌더링:

`Show-Markdown -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 문자열에서 콘솔로 Markdown 렌더링:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"# Markdown content"</span>` | Show-Markdown`

- 브라우저에서 Markdown 파일 열기:

`Show-Markdown -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -UseBrowser`
