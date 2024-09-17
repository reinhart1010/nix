---
layout: page
title: common/chatgpt (Indonesia)
description: "Skrip syel untuk memakai OpenAI ChatGPT dan DALL-E dalam terminal."
content_hash: 20170848e34ca4fc0ee53099229bb9cc63507928
last_modified_at: 2024-09-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chatgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chatgpt

Skrip syel untuk memakai OpenAI ChatGPT dan DALL-E dalam terminal.
Informasi lebih lanjut: <https://github.com/0xacx/chatGPT-shell-cli>.

- Jalankan dalam mode percakapan interaktif:

`chatgpt`

- Berikan [p]rompt (pertanyaan) untuk dijawab oleh sang model:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bagaimana cara membuat kriteria ekspresi reguler untuk mencocokkan format alamat surel/email?</span>`"`

- Jalankan dalam mode interaktif menggunakan suatu [m]odel (model default adalah `gpt-3.5-turbo`):

`chatgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-4</span>

- Jalankan dalam mode interaktif dengan [i]nitial prompt, perintah/permintaan awal yang dapat mendefinisikan jenis jawaban yang diharapkan dari sang model:

`chatgpt --init-prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Anda adalah Rick, dari serial Rick and Morty. Tanggapi pertanyaan dengan gayanya dan menyertakan lelucon yang menghina.</span>`"`

- Alihkan luaran dari program baris perintah lainnya sebagai pertanyaan masukan (prompt) kepada `chatgpt`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bagaimana cara melihat proses yang berjalan di Ubuntu?</span>`" | chatgpt`

- Generate an image using DALL-E:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image: Seekor kucing putih</span>`"`
