---
layout: page
title: common/prosodyctl (한국어)
description: "Prosody XMPP 서버의 제어 도구."
content_hash: 8fc7f596ab64fdc04b3fa4eb2846b5164343b35b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/prosodyctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prosodyctl

Prosody XMPP 서버의 제어 도구.
참고: `prosodyctl`을 통한 프로세스 관리는 권장되지 않습니다. 대신, 시스템에서 제공하는 도구(예: `systemctl`)를 사용하세요.
더 많은 정보: <https://prosody.im/doc/prosodyctl>.

- Prosody 서버의 상태 표시:

`sudo prosodyctl status`

- 서버의 구성 파일 다시 로드:

`sudo prosodyctl reload`

- Prosody XMPP 서버에 사용자 추가:

`sudo prosodyctl adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- 사용자의 비밀번호 설정:

`sudo prosodyctl passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- 사용자를 영구적으로 삭제:

`sudo prosodyctl deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>
