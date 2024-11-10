---
layout: page
title: linux/mssh (한국어)
description: "여러 SSH 서버와 동시에 상호작용할 수 있는 GTK+ 기반 SSH 클라이언트."
content_hash: b861c15ad4187d75b07c48bcfabe022c5864fdf5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mssh

여러 SSH 서버와 동시에 상호작용할 수 있는 GTK+ 기반 SSH 클라이언트.
더 많은 정보: <https://manned.org/mssh>.

- 새 창을 열고 여러 SSH 서버에 연결:

`mssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자@호스트1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자@호스트2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- `~/.mssh_clusters`에 미리 정의된 서버 그룹에 새 창에서 연결:

`mssh --alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_이름</span>
