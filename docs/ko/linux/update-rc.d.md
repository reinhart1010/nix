---
layout: page
title: linux/update-rc.d (한국어)
description: "System-V 스타일의 init 스크립트 링크를 설치하고 제거합니다."
content_hash: f66edcb9a24b0c577220f5f1002e4590e7196319
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/update-rc.d.html
    icon: bi bi-globe
tldri18n_status: 2
---
# update-rc.d

System-V 스타일의 init 스크립트 링크를 설치하고 제거합니다.
Init 스크립트는 `/etc/init.d/`에 있습니다.
더 많은 정보: <https://manned.org/update-rc.d>.

- 서비스 설치:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` defaults`

- 서비스 활성화:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` enable`

- 서비스 비활성화:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` disable`

- 서비스를 강제로 제거:

`update-rc.d -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` remove`
