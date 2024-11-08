---
layout: page
title: linux/efibootmgr (한국어)
description: "UEFI 부트 매니저를 조작합니다."
content_hash: a35d9b35978b37ec106fe57c76ebe2b5c459e4c2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/efibootmgr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/efibootmgr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># efibootmgr

UEFI 부트 매니저를 조작합니다.
더 많은 정보: <https://manned.org/efibootmgr>.

- 부트 옵션과 해당 번호를 모두 나열:

`efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unicode</span>

- UEFI Shell v2를 부트 옵션으로 추가:

`sudo efibootmgr -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -l "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\경로\대상\shell.efi</span>`" -L "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI Shell</span>`"`

- Linux를 부트 옵션으로 추가:

`sudo efibootmgr --create --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` --part `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --loader "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\vmlinuz</span>`" --unicode "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_cmdline</span>`" --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Linux</span>`"`

- 현재 부트 순서 변경:

`sudo efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--bootorder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0002,0008,0001,0005</span>

- 부트 옵션 삭제:

`sudo efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--bootnum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0008</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-B|--delete-bootnum</span>
