---
layout: page
title: common/picom-trans (한국어)
description: "`picom` 윈도우 합성기의 윈도우 투명도를 설정."
content_hash: ad72a70237c27d79141c696292e3caabc28e786b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/picom-trans.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picom-trans

`picom` 윈도우 합성기의 윈도우 투명도를 설정.
더 많은 정보: <https://github.com/yshui/picom>.

- 현재 포커스된 윈도우의 투명도를 특정 퍼센트로 설정:

`picom-trans --current --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- 특정 이름을 가진 윈도우의 투명도를 설정:

`picom-trans --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Firefox</span>` --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- 마우스 커서로 선택한 특정 윈도우의 투명도를 설정:

`picom-trans --select --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- 특정 윈도우의 투명도를 토글:

`picom-trans --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Firefox</span>` --toggle`
