---
layout: page
title: common/mods (한국어)
description: "파이프라인을 위해 설계된 커맨드라인 AI."
content_hash: 9b03d979cc3851ab3e2348725ea8d408c1aa3d92
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mods.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mods

파이프라인을 위해 설계된 커맨드라인 AI.
더 많은 정보: <https://github.com/charmbracelet/mods>.

- 일반적인 질문하기:

`mods "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오리너구리에 대한 시를 써 줘</span>`"`

- `$EDITOR`에서 설정 열기:

`mods --settings`

- 코드에 대한 의견을 마크다운 형식으로 요청하기:

`mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이 코드를 개선하기 위한 의견은?</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문서화 도움을 마크다운 형식으로 요청하기:

`mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r을 누르면 무료 토끼를 보내주는 기능에 대한 새로운 섹션을 이 README에 작성해 줘</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">README.md</span>

- 비디오를 마크다운 형식으로 정리하기:

`ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오</span>` | mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이를 시대별로 정리하고 요약해 줘</span>`"`

- 원시 HTML을 읽고 내용을 마크다운 형식으로 요약하기:

`curl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m</span>`" | mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이 날씨 데이터를 사람을 위해 요약해 줘</span>`"`

- 도움말 표시:

`mods --help`
