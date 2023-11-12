---
layout: page
title: windows/invoke-webrequest (Indonesia)
description: "Membuat panggilan dan permintaan HTTP/HTTPS."
content_hash: 065e17303b227b91730560393c5b21eaff84c150
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/invoke-webrequest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Invoke-WebRequest

Membuat panggilan dan permintaan HTTP/HTTPS.
Perintah ini hanya dapat digunakan dalam PowerShell.
Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Unduh konten URL ke file:

`Invoke-WebRequest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -OutFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Kirim data form yang telah di encode (permintaan POST atau tipe data `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Kirim sebuah permintaan dengan header tambahan, menggunakan metode HTTP kustom:

`Invoke-WebRequest -Headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@{ X-My-Header = '123' }</span>` -Method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Kirim data dalam format JSON, Menentukan jenis konten yang sesuai header:

`Invoke-WebRequest -Body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>`  -ContentType 'application/json' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- Berikan nama pengguna dan kata sandi untuk otentikasi server:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
