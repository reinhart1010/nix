---
layout: page
title: common/rails-db (Indonesia)
description: "Beragam subperintah yang berkaitan dengan database untuk Rauby on Rails."
content_hash: b0a85fd4226f6d0611c73aa4164e01fd4bd85d86
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rails-db.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails db

Beragam subperintah yang berkaitan dengan database untuk Rauby on Rails.
Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html>.

- Membuat database, memuat skema dan menginisiasinya dengan data awal:

`rails db:setup`

- Mengakses konsol database:

`rails db`

- Membuat database yang didefinisikan di environment saat ini:

`rails db:create`

- Menghapus database yang didefinisikan di environment saat ini:

`rails db:drop`

- Menjalankan migrasi yang belum:

`rails db:migrate`

- Menampilkan status dari masing-masing file migrasi:

`rails db:migrate:status`

- Rollback ke migrasi sebelumnya:

`rails db:rollback`

- Mengisi database dengan data yang didefinisikan di `db/seeds.rb`:

`rails db:seed`
