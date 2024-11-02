---
layout: page
title: windows/reg-export (한국어)
description: "지정된 하위 키와 값을 `.reg` 파일로 내보냅니다."
content_hash: 81813d968faa71426ea3473cc47c5508fccdf58c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/reg-export.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-export.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/reg-export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reg export

지정된 하위 키와 값을 `.reg` 파일로 내보냅니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- 특정 키의 모든 하위 키와 값을 내보내기:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.reg</span>

- 기존 파일을 강제로 ([y]es로 가정) 덮어쓰기:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.reg</span>` /y`
