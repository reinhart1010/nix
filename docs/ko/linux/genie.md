---
layout: page
title: linux/genie (한국어)
description: "WSL(Windows Subsystem for Linux)에서 systemd를 실행하기 위해 \"bottle\" 네임스페이스를 설정하고 사용합니다."
content_hash: a67ff653a442e8bcf10ab71bd54074a3ae135af8
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/genie.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/genie.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># genie

WSL(Windows Subsystem for Linux)에서 systemd를 실행하기 위해 "bottle" 네임스페이스를 설정하고 사용합니다.
이미 실행 중인 배포판이 아닌 Windows에서 이를 실행하려면 `wsl`을 앞에 붙입니다.
더 많은 정보: <https://github.com/arkane-systems/genie>.

- 보틀 초기화 (시작 시 한 번 실행):

`genie -i`

- 보틀 내부에서 로그인 셸 실행:

`genie -s`

- 보틀 내부에서 특정 명령 실행:

`genie -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
