---
layout: page
title: common/diff (Türkçe)
description: "Dosyaları ve dizinleri karşılaştırın."
content_hash: 11a1ead44bbb763fbb7616d6ccec0c33117d2306
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diff

Dosyaları ve dizinleri karşılaştırın.
Daha fazla bilgi için: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Dosyaları karşılaştır (`eski_dosya`'yı `yeni_dosya`'ya dönüştürmek için yapılan değişiklikleri listeler):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya</span>

- Boşlukları yok sayarak dosyaları karşılaştırın:

`diff --ignore-all-space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya</span>

- Farkları yan yana göstererek dosyaları karşılaştırın:

`diff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya</span>

- Farkları birleştirilmiş biçimde (`git diff` tarafından kullanıldığı gibi) göstererek dosyaları karşılaştırın:

`diff --unified `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya</span>

- Dizinleri yinelemeli olarak karşılaştırın (farklı dosya/dizin adlarını ve dosyalarda yapılan değişiklikleri gösterir):

`diff --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dizin</span>

- Dizinleri karşılaştırın, yalnızca farklı olan dosyaların adlarını gösterin:

`diff --recursive --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dizin</span>

- Git için iki metin dosyasının farklarından, var olmayan dosyaları ise boş olarak değerlendirerek bir yama dosyası oluşturun:

`diff --text --unified --new-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fark.patch</span>
