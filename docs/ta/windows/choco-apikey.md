---
layout: page
title: windows/choco-apikey (தமிழ்)
description: "சாக்லேட்டி மூலங்களுக்கான API விசைகளை நிர்வகிக்கவும்."
content_hash: 2b3a787104caee5c19af5da9c2109e411322648c
last_modified_at: 2024-05-09
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco apikey

சாக்லேட்டி மூலங்களுக்கான API விசைகளை நிர்வகிக்கவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-apikey>.

- ஆதாரங்களின் பட்டியலையும் அவற்றின் API விசைகளையும் காட்டவும்:

`choco apikey`

- ஒரு குறிப்பிட்ட மூலத்தையும் அதன் API விசையையும் காண்பி:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல_முகவரி</span>`"`

- மூலத்திற்கான API விசையை அமைக்கவும்:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல_முகவரி</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key</span>`"`

- மூலத்திற்கான API விசையை அகற்றவும்:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல_முகவரி</span>`" --remove`
