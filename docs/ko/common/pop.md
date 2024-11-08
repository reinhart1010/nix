---
layout: page
title: common/pop (한국어)
description: "터미널에서 이메일을 보내는 도구."
content_hash: 8c5b91fc61e48407d8c6dc60560ecb985e176b53
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pop

터미널에서 이메일을 보내는 도구.
더 많은 정보: <https://github.com/charmbracelet/pop>.

- 텍스트 기반 사용자 인터페이스 시작:

`pop`

- Markdown 파일의 내용을 본문으로 사용하여 이메일 보내기:

`pop < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메시지.md</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>` --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">you@example.com</span>` --subject "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오리에 대한 주제</span>`" --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첨부파일</span>

- 도움말 표시:

`pop --help`
