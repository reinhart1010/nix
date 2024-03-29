---
layout: page
title: windows/choco-source (தமிழ்)
description: "சாக்லேட்டி மூலம் தொகுப்புகளுக்கான ஆதாரங்களை நிர்வகிக்கவும்."
content_hash: a388a25da9381aac04c4b5259b1a0b099bace969
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-source.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-source.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-source.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-source.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

சாக்லேட்டி மூலம் தொகுப்புகளுக்கான ஆதாரங்களை நிர்வகிக்கவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-source>.

- தற்போது கிடைக்கக்கூடிய ஆதாரங்களை பட்டியலிடுங்கள்:

`choco source list`

- புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- நற்சான்றிதழ்களுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பயனர்பெயர்</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடவுச்சொல்</span>

- கிளையன்ட் சான்றிதழுடன் புதிய தொகுப்பு மூலத்தைச் சேர்க்கவும்:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சான்றிதழ்\பாதை</span>

- தொகுப்பு மூலத்தை இயக்கு:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- ஒரு தொகுப்பு மூலத்தை முடக்கு:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- தொகுப்பு மூலத்தை அகற்றவும்:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>
