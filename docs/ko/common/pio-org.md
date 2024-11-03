---
layout: page
title: common/pio-org (한국어)
description: "PlatformIO 조직 및 소유자를 관리."
content_hash: bc5e30e4767de477206641172af3c3245ce9884a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-org.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-org.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio org

PlatformIO 조직 및 소유자를 관리.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- 새 조직 생성:

`pio org create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>

- 조직 삭제:

`pio org destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>

- 사용자 조직에 추가:

`pio org add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 사용자 조직에서 제거:

`pio org remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 현재 사용자가 멤버로 있는 모든 조직 및 소유자 나열:

`pio org list`

- 조직의 이름, 이메일 또는 표시 이름 업데이트:

`pio org update --orgname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_조직_이름</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_이메일</span>` --displayname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_표시_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>
