---
layout: page
title: linux/mesg (한국어)
description: "터미널이 다른 사용자로부터 메시지를 수신할 수 있는지 확인하거나 설정합니다. 주로 `write` 명령에서 사용됩니다."
content_hash: e6c072c167bcb73be42f07903809829ce931db36
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mesg

터미널이 다른 사용자로부터 메시지를 수신할 수 있는지 확인하거나 설정합니다. 주로 `write` 명령에서 사용됩니다.
같이 보기: `write`, `talk`.
더 많은 정보: <https://manned.org/mesg.1>.

- 터미널의 메시지 수신 가능 여부 확인:

`mesg`

- 다른 사용자로부터 메시지 수신 거부:

`mesg n`

- 다른 사용자로부터 메시지 수신 허용:

`mesg y`

- [v]자세히 모드를 활성화하여 터미널에서 실행되지 않을 경우 경고 출력:

`mesg --verbose`
