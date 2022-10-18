---
layout: page
title: common/gh (Indonesia)
description: "Memudahkan pengaksesan GitHub dari command-line."
content_hash: b899a23a5c70d7b1ec9f94a33d6c9fc1694914ea
related_topics:
  - title: Deutsch version
    url: /de/common/gh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gh.html
    icon: bi bi-globe
---
# gh

Memudahkan pengaksesan GitHub dari command-line.
Beberapa subcommands seperti `gh config` memiliki dokumentasi sendiri.
Informasi lebih lanjut: <https://cli.github.com/>.

- Mengklon sebuah GitHub repositori di lokal:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pemilik</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repositori</span>

- Membuat isu baru:

`gh issue create`

- Melihat dan filter issue yang sedang open pada repositori:

`gh issue list`

- Melihat isu di browser:

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_isu</span>

- Membuat sebuah pull request:

`gh pr create`

- Melihat pull request di browser:

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_pr</span>

- Mengecek pada local branch sebuah pull request, diikuti dengan nomor pull requestnya:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_pr</span>

- Mengecek status pull request pada sebuah repository:

`gh pr status`
