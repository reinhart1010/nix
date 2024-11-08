---
layout: page
title: common/lpoptions (한국어)
description: "프린터 옵션 및 기본값 표시 또는 설정."
content_hash: 1c741d50dd025bc387d74dc2c9f6ed2db37eb4cd
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lpoptions.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpoptions.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpoptions

프린터 옵션 및 기본값 표시 또는 설정.
같이 보기: `lpadmin`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

- 기본 프린터 설정:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터[/인스턴스]</span>

- 특정 프린터의 프린터 전용 옵션 나열:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` -l`

- 특정 프린터에 새 옵션 설정:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>

- 특정 프린터의 옵션 제거:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` -x`
