---
layout: page
title: windows/taskkill (한국어)
description: "프로세스 아이디 또는 이름으로 프로세스를 종료합니다."
content_hash: c8ef6c469c0706838dee346ee0ec2d6640022085
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/taskkill.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/taskkill.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/taskkill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/taskkill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># taskkill

프로세스 아이디 또는 이름으로 프로세스를 종료합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 프로세스 아이디로 프로세스 종료:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 프로세스 이름으로 프로세스 종료:

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 강제로 지정된 프로세스 종료:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>` /f`

- 프로세스 및 자식 프로세스 종료:

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` /t`

- 원격 머신에서 프로세스 종료:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 명령어 사용 정보 표시:

`taskkill /?`
