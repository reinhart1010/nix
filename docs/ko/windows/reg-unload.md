---
layout: page
title: windows/reg-unload (한국어)
description: "`reg load` 명령을 사용하여 로드된 레지스트리에서 데이터를 제거."
content_hash: edc829a58471503789e58925e9199df3a3aac595
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/reg-unload.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-unload.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/reg-unload.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reg unload

`reg load` 명령을 사용하여 로드된 레지스트리에서 데이터를 제거.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-unload>.

- 지정된 키에 대한 레지스트리 데이터 제거:

`reg unload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>
