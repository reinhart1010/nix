---
layout: page
title: linux/gsettings (한국어)
description: "스키마 검증을 통해 dconf 설정을 조회하고 수정."
content_hash: 9ecdf92020cf813238445dee17a95265bb9d27bf
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/gsettings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/gsettings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gsettings

스키마 검증을 통해 dconf 설정을 조회하고 수정.
더 많은 정보: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- 키의 값을 설정 (키가 존재하지 않거나 값이 범위를 벗어난 경우 실패):

`gsettings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제-키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 키의 값 또는 `dconf`에 설정되지 않은 경우 스키마에 제공된 기본값 출력:

`gsettings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제-키</span>

- 키를 해제하여 스키마 기본값 사용:

`gsettings reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제-키</span>

- 모든 (이동 불가능한) 스키마, 키 및 값 표시:

`gsettings list-recursively`

- 하나의 스키마에서 모든 키 및 값 (설정되지 않은 경우 기본값) 표시:

`gsettings list-recursively `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>

- 키에 대해 스키마가 허용하는 값 표시 (enum 키에 유용):

`gsettings range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제-키</span>

- 키의 사람이 읽을 수 있는 설명 표시:

`gsettings describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제-키</span>
