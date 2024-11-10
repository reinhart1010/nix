---
layout: page
title: linux/rsh (한국어)
description: "원격 호스트에서 명령을 실행합니다."
content_hash: 86e2a874ed798e1e399b655fa38c36e70addfdd4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsh

원격 호스트에서 명령을 실행합니다.
더 많은 정보: <https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- 원격 호스트에서 명령 실행:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- 특정 사용자명으로 원격 호스트에서 명령 실행:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- 원격 호스트에서 명령을 실행할 때 `stdin`을 `/dev/null`로 리다이렉트:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` --no-err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
