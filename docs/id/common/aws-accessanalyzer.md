---
layout: page
title: common/aws-accessanalyzer (Indonesia)
description: "Analisa dan tinjau ulang kebijakan penggunaan sumber daya untuk melihat potensi risiko keamanan."
content_hash: bc97a6c9c2628c0b13323f2a2400d466f463ee52
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/common/aws-accessanalyzer.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-accessanalyzer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-accessanalyzer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-accessanalyzer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws accessanalyzer

Analisa dan tinjau ulang kebijakan penggunaan sumber daya untuk melihat potensi risiko keamanan.
Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- Buat suatu instansi Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_analyzer</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipe_analisis</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">daftar_tag</span>

- Hapus suatu instansi Access Analyzer:

`aws accessanalyzer delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>

- Tampilkan rincian tentang suatu instansi Access Analyzer:

`aws accessanalyzer get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>

- Tampilkan daftar seluruh instansi Access Analyzers:

`aws accessanalyzer list-analyzers`

- Mutakhirkan suatu aturan terhadap instansi Access Analyzer:

`aws accessanalyzer update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">daftar_tag_baru</span>

- Buat sebuah aturan bagi proses pengarsipan terhadap instansi Access Analyzer:

`aws accessanalyzer create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aturan</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter</span>

- Hapus suatu aturan pengarsipan bagi instansi Access Analyzer:

`aws accessanalyzer delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aturan</span>

- Tampilkan daftar seluruh aturan pengarsipan yang berlaku bagi suatu instansi Access Analyzer:

`aws accessanalyzer list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_analyzer</span>
