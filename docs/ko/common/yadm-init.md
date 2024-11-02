---
layout: page
title: common/yadm-init (한국어)
description: "새로운 빈 저장소를 초기화하여 dotfiles를 추적."
content_hash: e9791ac866ceb2106a2377412aa9259087b3164d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/yadm-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-init

새로운 빈 저장소를 초기화하여 dotfiles를 추적.
저장소는 `$HOME/.local/share/yadm/repo.git`에 저장됩니다.
더 많은 정보: <https://yadm.io/docs/getting_started>.

- 실행:

`yadm init`

- 작업 트리 덮어쓰기:

`yadm init -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업트리_폴더</span>

- 기존 저장소 덮어쓰기:

`yadm init -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_저장소</span>
