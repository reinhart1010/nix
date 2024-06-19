---
layout: page
title: common/arduino (Indonesia)
description: "Arduino Studio - Sebuah alat pengembangan piranti lunak (IDE) bagi platform Arduino."
content_hash: 89ce22b57a19a260f2233d49d7eaed551304c93e
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/arduino.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino

Arduino Studio - Sebuah alat pengembangan piranti lunak (IDE) bagi platform Arduino.
Informasi lebih lanjut: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Bangun piranti lunak dari suatu berkas (sketsa) kode sumber:

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.ino</span>

- Bangun dan pasang piranti lunak menuju perangkat Arduino:

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.ino</span>

- Bangun dan pasang piranti lunak menuju suatu perangkat Arduino Nano dengan prosesor Atmega328p yang terhubung dalam port `/dev/ttyACM0`:

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.ino</span>

- Atur `nilai` untuk suatu jenis preferensi/konfigurasi berdasarkan `nama` atau kata kunci:

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai</span>

- Bangun piranti lunak, kemudian simpan menuju suatu direktori hasil pembangunan, dan gunakan kembali hasil-hasil sebelumnya di dalam direktori tersebut:

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_hasil_pembangunan</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/bekas.ino</span>

- Simpan segala perubahan pada preferensi/konfigurasi menuju berkas `preferences.txt`:

`arduino --save-prefs`

- Pasang piranti pendukung pengembangan untuk perangkat Arduino berbasis SAM (seperti Arduino Due):

`arduino --install-boards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:sam</span>`"`

- Pasang pustaka piranti lunak (library) untuk Bridge dan Servo:

`arduino --install-library "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bridge:1.0.0,Servo:1.2.0</span>`"`
