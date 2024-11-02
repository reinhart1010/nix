---
layout: page
title: windows/move (한국어)
description: "파일 및 디렉토리를 이동 또는 이름을 변경합니다."
content_hash: b3503ca3e5d8f1ab142582427eba03cbaa412596
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/move.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/move.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/move.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># move

파일 및 디렉토리를 이동 또는 이름을 변경합니다.
PowerShell에서 이 명령어는 `Move-Item`의 별칭입니다. 이 문서는 `move`의 Command Prompt (`cmd`) 버전을 기준으로 작성되었습니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- 동등한 PowerShell 명령어 문서 보기:

`tldr move-item`

- 목표가 기존 디렉토리가 아닐 때 파일 또는 디렉토리 이름 변경:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\목표</span>

- 파일 또는 디렉토리를 기존 디렉토리로 이동:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\기존_디렉토리</span>

- 드라이브 간에 파일 또는 디렉토리 이동:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:\경로\대상\목표</span>

- 기존 파일을 덮어쓰기 전에 확인 메시지를 표시 안함:

`move /Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\기존_디렉토리</span>

- 기존 파일을 덮어쓰기 전에 확인 메시지를 표시, 파일 권한과 관계없이:

`move /-Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\기존_디렉토리</span>
