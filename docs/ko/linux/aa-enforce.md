---
layout: page
title: linux/aa-enforce (한국어)
description: "AppArmor 프로파일을 강제 모드로 설정합니다."
content_hash: e87b27bf63895faf173853ee014afd7cd39e61f6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/aa-enforce.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-enforce.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-enforce

AppArmor 프로파일을 강제 모드로 설정합니다.
같이 보기: `aa-complain`, `aa-disable`, `aa-status`.
더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- 프로파일 활성화:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로파일</span>

- 여러 프로파일 활성화:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로파일1 경로/대상/프로파일2 ...</span>
