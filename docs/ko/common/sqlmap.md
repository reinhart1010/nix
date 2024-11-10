---
layout: page
title: common/sqlmap (한국어)
description: "SQL 인젝션 취약점을 탐지하고 악용."
content_hash: 8cdcce65da04e7dd5fb99c9bdbb559d62a5fc893
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sqlmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqlmap

SQL 인젝션 취약점을 탐지하고 악용.
더 많은 정보: <https://sqlmap.org>.

- 단일 대상 URL에 대해 sqlmap 실행:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php?id=1</span>`"`

- POST 요청으로 데이터 전송 (`--data`는 POST 요청을 의미):

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --data="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id=1</span>`"`

- 매개변수 구분자 변경 (기본값은 &):

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --data="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query=foobar;id=1</span>`" --param-del="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`"`

- `./txt/user-agents.txt`에서 무작위 `User-Agent` 선택 및 사용:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --random-agent`

- HTTP 프로토콜 인증을 위한 사용자 자격 증명 제공:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Basic</span>` --auth-cred "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser:testpass</span>`"`
