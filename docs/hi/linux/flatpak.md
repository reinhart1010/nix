---
layout: page
title: linux/flatpak (हिन्दी)
description: "फ्लैटपैक अनुप्रयोग और रनटाइम बनाएं, स्थापित करें और चलाएं।"
content_hash: 17260b462fb894d87dda4e99452518f47a5ba349
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
---
# flatpak

फ्लैटपैक अनुप्रयोग और रनटाइम बनाएं, स्थापित करें और चलाएं।
अधिक जानकारी: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>।

- एक स्थापित अनुप्रयोग चलाएं:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>

- दूरस्थ स्रोत से एक अनुप्रयोग स्थापित करें:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">दूरस्थ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>

- सभी स्थापित अनुप्रयोग और रनटाइम की सूची दिखाएं:

`flatpak list`

- सभी स्थापित अनुप्रयोग और रनटाइम को अद्यतित करें:

`flatpak update`

- एक दूरस्थ स्रोत जोड़ें:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">दूरस्थ_नाम</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">दूरस्थ_URL</span>

- एक स्थापित अनुप्रयोग हटाएं:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>

- सभी अउपयोग नहीं किए जा रहे अनुप्रयोग हटाएं:

`flatpak remove --unused`

- एक स्थापित अनुप्रयोग के बारे में जानकारी दिखाएं:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>
