---
layout: page
title: linux/run0 (한국어)
description: "권한을 대화식으로 상승시킵니다."
content_hash: 63b34b39d940ec90c4018643a11438ea1a1d2cf9
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/run0.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/run0.html
    icon: bi bi-globe
tldri18n_status: 2
---
# run0

권한을 대화식으로 상승시킵니다.
`sudo`와 유사하지만, SUID 바이너리가 아니며 인증은 polkit을 통해 이루어지고 명령어는 `systemd` 서비스에서 호출됩니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- 명령어를 루트 사용자로 실행:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 다른 사용자 및/또는 그룹으로 명령어 실행:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|uid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름|gid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
