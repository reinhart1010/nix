---
layout: page
title: linux/exif (Indonesia)
description: "Lihat dan ubah informasi metadata EXIF pada berkas-berkas JPEG."
content_hash: e487f41e3762d69f877b1bc84ad133ab4133b0e9
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/exif.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/exif.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exif

Lihat dan ubah informasi metadata EXIF pada berkas-berkas JPEG.
Informasi lebih lanjut: <https://github.com/libexif/exif/>.

- Tampilkan daftar informasi EXIF yang terdapat pada suatu berkas gambar:

`exif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/gambar.jpg</span>

- Tampilkan daftar jenis tag informasi EXIF dalam format tabel, termasuk apakah tag tersebut terdapat dalam suatu gambar:

`exif --list-tags --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gambar.jpg</span>

- Ekstrak gambar pratinjau (thumbnail) dari suatu gambar menuju `thumbnail.jpg`:

`exif --extract-thumbnail --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thumbnail.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gambar.jpg</span>

- Tampilkan isi mentahan terhadap tag metadata "Model" dalam suatu gambar:

`exif --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Model</span>` --machine-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gambar.jpg</span>

- Ganti nilai tag metadata "Artist" menjadi John Smith, dan simpan perubahan menuju berkas baru di `new.jpg`:

`exif --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.jpg</span>` --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Artist</span>`" --set-value="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">John Smith</span>`" --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gambar.jpg</span>
