---
layout: page
title: linux/distrobox-export (한국어)
description: "컨테이너에서 호스트 OS로 앱/서비스/바이너리를 내보냅니다. 같이 보기: `tldr distrobox`."
content_hash: 66b476daa32720e729cde16e04207f2cd8042608
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/distrobox-export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-export.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-export

컨테이너에서 호스트 OS로 앱/서비스/바이너리를 내보냅니다. 같이 보기: `tldr distrobox`.
더 많은 정보: <https://distrobox.it/usage/distrobox-export>.

- 컨테이너에서 호스트로 앱 내보내기 (데스크톱 항목/아이콘이 호스트 시스템의 응용 프로그램 목록에 나타납니다):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --extra-flags "--foreground"`

- 컨테이너에서 호스트로 바이너리 내보내기:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/호스트_바이너리</span>

- 컨테이너에서 호스트로 바이너리 내보내기 (예: `$HOME/.local/bin`):

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/내보내기</span>

- 컨테이너에서 호스트로 서비스 내보내기 (`--sudo`는 해당 서비스를 컨테이너 내에서 루트 권한으로 실행):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --extra-flags "--allow-newer-config" --sudo`

- 내보낸 응용 프로그램 제거/삭제:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --delete`
