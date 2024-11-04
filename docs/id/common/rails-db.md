---
layout: page
title: common/rails-db (Indonesia)
description: "Beragam subperintah yang berkaitan dengan database untuk Rauby on Rails."
content_hash: d201a2a3c04a0b1a3b44fe872a939dbcd08aa23a
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/rails-db.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails db

Beragam subperintah yang berkaitan dengan database untuk Rauby on Rails.
Informasi lebih lanjut: <https://guides.rubyonrails.org/active_record_migrations.html>.

- Buat pangkalan data (database) baru, memuat skema dan menginisiasinya dengan data awal:

`rails db:setup`

- Akses konsol database:

`rails db`

- Buat database yang didefinisikan di environment saat ini:

`rails db:create`

- Hapus database yang didefinisikan di environment saat ini:

`rails db:drop`

- Jalankan migrasi yang belum:

`rails db:migrate`

- Tampilkan status dari masing-masing file migrasi:

`rails db:migrate:status`

- Rollback ke migrasi sebelumnya:

`rails db:rollback`

- Isi database dengan data yang didefinisikan di `db/seeds.rb`:

`rails db:seed`
