---
layout: page
title: common/tldr (தமிழ்)
description: "tldr-pages திட்டத்தில் இருந்து கட்டளை வரி கருவிகளுக்கான எளிய உதவிப் பக்கங்களைக் காண்பிக்கவும்."
content_hash: 2ace7efa2983695f5badc7c3c109dded43557ea9
last_modified_at: 2023-11-26
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tldr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tldr

tldr-pages திட்டத்தில் இருந்து கட்டளை வரி கருவிகளுக்கான எளிய உதவிப் பக்கங்களைக் காண்பிக்கவும்.
குறிப்பு: வாடிக்கையாளர் விவரக்குறிப்பிற்கு `--language` மற்றும் `--list` விருப்பங்கள் தேவையில்லை, ஆனால் பெரும்பாலான வாடிக்கையாளர்கள் அவற்றைச் செயல்படுத்துகிறார்கள்.
மேலும் விவரத்திற்கு: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- ஒரு குறிப்பிட்ட கட்டளைக்கு `tldr` பக்கத்தை அச்சிடுங்கள் (குறிப்பு: நீங்கள் இப்படி தான் இங்கு வந்தீர்கள்!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- ஒரு குறிப்பிட்ட துணைக் கட்டளைக்கு `tldr` பக்கத்தை அச்சிடுக:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">துணை_கட்டளை</span>

- கொடுக்கப்பட்ட [L] மொழியில் கட்டளைக்காக `tldr` பக்கத்தை அச்சிடவும் (கிடைத்தால், இல்லையெனில் ஆங்கிலத்திற்குத் திரும்பவும்):

`tldr --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மொழி_குறியீடு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- ஒரு குறிப்பிட்ட [p] தளத்திலிருந்து ஒரு கட்டளைக்கு `tldr` பக்கத்தை அச்சிடவும்:

`tldr --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- `tldr` பக்கங்களின் உள்ளூர் தற்காலிக சேமிப்பை [u] புதுப்பிக்கவும்:

`tldr --update`

- தற்போதைய இயங்குதளத்திற்கான அனைத்து பக்கங்களையும் பட்டியலிடவும் மற்றும் `common`:

`tldr --list`
