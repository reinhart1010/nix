---
layout: page
title: windows/reg-restore (한국어)
description: "네이티브 `.hiv` 파일에서 키와 그 값을 복원."
content_hash: 2f0592438e4b017a1d08633760230544d717b18b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/reg-restore.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/reg-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reg restore

네이티브 `.hiv` 파일에서 키와 그 값을 복원.
자세한 내용은 `reg-save`를 참조하세요.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-restore>.

- 백업 파일의 데이터로 지정된 키 덮어쓰기:

`reg restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.hiv</span>
