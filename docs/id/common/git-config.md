---
layout: page
title: common/git-config (Indonesia)
description: "Ubah pengaturan Git untuk repositori-repositori tertentu."
content_hash: ee1eb14e5c03b9efeb50c2319f3aaaaff4d277af
last_modified_at: 2024-06-11
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git config

Ubah pengaturan Git untuk repositori-repositori tertentu.
Konfigurasi ini dapat diatur hanya untuk repositori saat ini (lokal/local) atau untuk pengguna sistem operasi saat ini (global).
Informasi lebih lanjut: <https://git-scm.com/docs/git-config>.

- Tampilkan hanya daftar pengaturan Git untuk repositori saat ini (sebagaimana tersimpan dalam `.git/config` dalam pangkal direktori repositori):

`git config --list --local`

- Tampilkan hanya daftar pengaturan Git untuk pengguna saat ini (sebagaimana tersimpan dalam `~/.gitconfig` sebagai default, atau bila ada, `$XDG_CONFIG_HOME/git/config`):

`git config --list --global`

- Tampilkan hanya daftar pengaturan Git untuk keseluruhan sistem operasi (sebagaimana tersimpan dalam `/etc/gitconfig`), dan tampilkan lokasi berkas tersebut:

`git config --list --system --show-origin`

- Tampilkan nilai atas entri konfigurasi saat ini (contoh: `alias.unstage`):

`git config alias.unstage`

- Simpan baru atau ubah nilai entri konfigurasi tertentu secara global (untuk pengguna saat ini):

`git config --global alias.unstage "reset HEAD --"`

- Hapus atau kembalikan nilai dari entri konfigurasi tersebut menuju nilai default (bila ada):

`git config --global --unset alias.unstage`

- Sunting konfigurasi Git pada repositori saat ini dengan aplikasi pengolah teks default:

`git config --edit`

- Sunting konfigurasi Git pada pengguna saat ini dengan aplikasi pengolah teks default:

`git config --global --edit`
