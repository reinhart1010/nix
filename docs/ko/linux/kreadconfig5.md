---
layout: page
title: linux/kreadconfig5 (한국어)
description: "KDE Plasma의 KConfig 항목 읽기."
content_hash: e501a10f49f17ac2d725e96bda614a157e861307
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/kreadconfig5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kreadconfig5

KDE Plasma의 KConfig 항목 읽기.
더 많은 정보: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- 전역 설정에서 키 읽기:

`kreadconfig5 --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- 특정 설정 파일에서 키 읽기:

`kwriteconfig5 --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- systemd가 Plasma 세션을 시작하는지 확인:

`kreadconfig5 --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">startkderc</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">General</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemdBoot</span>
