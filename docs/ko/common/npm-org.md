---
layout: page
title: common/npm-org (한국어)
description: "조직을 관리."
content_hash: b338e8bbdae989b66d160cc844b4843663d5f0fa
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/npm-org.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm-org

조직을 관리.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-org>.

- 조직에 새 사용자 추가:

`npm org set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 조직 내 사용자의 역할 변경:

`npm org set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">developer|admin|owner</span>

- 조직에서 사용자 제거:

`npm org rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 조직의 모든 사용자 나열:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>

- 조직의 모든 사용자를 JSON 형식으로 나열:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` --json`

- 조직 내 사용자의 역할 표시:

`npm org ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
