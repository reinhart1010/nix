---
layout: page
title: linux/kexec (한국어)
description: "새 커널로 직접 재부팅."
content_hash: 925c64ff04008dade7dc4c212b9042298b7640a9
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/kexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kexec

새 커널로 직접 재부팅.
더 많은 정보: <https://manned.org/kexec>.

- 새 커널 로드:

`kexec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/커널</span>` --initrd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/initrd</span>` --command-line=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자들</span>

- 현재 부팅 매개변수로 새 커널 로드:

`kexec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/커널</span>` --initrd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/initrd</span>` --reuse-cmdline`

- 현재 로드된 커널 실행:

`kexec -e`

- 현재 kexec 대상 커널 언로드:

`kexec -u`
