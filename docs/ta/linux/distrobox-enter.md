---
layout: page
title: linux/distrobox-enter (தமிழ்)
description: "டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உள்ளிடவும். மேலும் காண்க: `tldr distrobox`."
content_hash: 78f733e7b1627cc73eda6cb3958ac61239173afa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உள்ளிடவும். மேலும் காண்க: `tldr distrobox`.
இயக்கப்படும் இயல்புநிலை கட்டளை உங்கள் SHELL, நீங்கள் இயக்குவதற்கு வெவ்வேறு ஓடுகள் அல்லது முழு கட்டளைகளையும் குறிப்பிடலாம். ஸ்கிரிப்ட், பயன்பாடு அல்லது சேவையில் பயன்படுத்தினால், `--headless' பயன்முறையைப் பயன்படுத்தி tty மற்றும் ஊடாடும் தன்மையை முடக்கலாம்.
மேலும் விவரத்திற்கு: <https://distrobox.privatedns.org/usage/distrobox-enter.html>.

- டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உள்ளிடவும்:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>

- டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உள்ளிட்டு, உள்நுழையும்போது கட்டளையை இயக்கவும்:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- ஒரு tty ஐ உடனுக்குடன் இல்லாமல் ஒரு டிஸ்ட்ரோபாக்ஸ் கொள்கலனை உள்ளிடவும்:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
