---
layout: page
title: linux/gio-trash (한국어)
description: "파일을 휴지통으로 이동합니다."
content_hash: b8601fc43a9ca5f66f1b96c55ba0c5892170f177
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/gio-trash.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/gio-trash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gio trash

파일을 휴지통으로 이동합니다.
GNOME에서 휴지통을 관리하는 데 사용됩니다.
더 많은 정보: <https://manned.org/gio.1>.

- 특정 파일을 휴지통으로 이동:

`gio trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 휴지통 항목 나열:

`gio trash --list`

- ID를 사용하여 휴지통에서 특정 항목 복원:

`gio trash trash://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
