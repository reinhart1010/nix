---
layout: page
title: linux/secret-tool (한국어)
description: "`libsecret` 패키지의 일부로 비밀번호를 저장하고 검색."
content_hash: c55a24a1618ca42185ef4025819617d0f03872cd
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/secret-tool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# secret-tool

`libsecret` 패키지의 일부로 비밀번호를 저장하고 검색.
`gnome-keyring`과 같은 Freedesktop 비밀 서비스 구현과 통신.
더 많은 정보: <https://gnome.pages.gitlab.gnome.org/libsecret/>.

- 선택적 레이블과 함께 비밀 저장:

`secret-tool store --label=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 비밀 검색:

`secret-tool lookup key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 비밀에 대한 추가 정보 얻기:

`secret-tool search key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 저장된 비밀 삭제:

`secret-tool clear key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>
