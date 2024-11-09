---
layout: page
title: common/bq (Indonesia)
description: "Alat pemrosesan data berbasis Python untuk BigQuery, layanan pergudangan data Google Cloud yang sepenuhnya terkelola dan bersifat serverless."
content_hash: 31f2fff4923f13054af3b9931bc94be99c8962f7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/bq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bq

Alat pemrosesan data berbasis Python untuk BigQuery, layanan pergudangan data Google Cloud yang sepenuhnya terkelola dan bersifat serverless.
Informasi lebih lanjut: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Jalankan suatu perintah kueri terhadap suatu tabel BigQuery dalam format SQL dasar, tambahkan opsi `--dry_run` untuk menaksir jumlah bita yang akan dibaca pada proses eksekusi:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAMA_DATASET</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAMA_TABEL</span>`'`

- Jalankan suatu perintah kueri dengan kumpulan parameter:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Buat suatu dataset atau tabel pada wilayah layanan Amerika Serikat (US):

`bq mk --location=US `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_tabel</span>

- Tampilkan seluruh dataset pada suatu proyek:

`bq ls --filter labels.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` --max_results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>` --format=prettyjson --project_id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_proyek</span>

- Lakukan proses pemuatan data secara batch dari berkas tertentu dalam format seperti CSV, JSON, Parquet, dan Avro ke dalam suatu tabel:

`bq load --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi</span>` --source_format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CSV|JSON|PARQUET|AVRO</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan_menuju_sumber</span>

- Salin suatu tabel menuju tabel lainnya:

`bq cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TABEL_LAMA</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabel_baru</span>

- Tampilkan bantuan:

`bq help`
