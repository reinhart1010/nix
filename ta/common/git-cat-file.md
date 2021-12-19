---
layout: page
title: common/git-cat-file (தமிழ்)
description: "கிட் களஞ்சிய பொருள்களுக்கான உள்ளடக்கம் அல்லது வகை மற்றும் அளவு தகவல்களை வழங்கவும்."
content_hash: a61f99f36adac0744121d56a205e8616477f1bd9
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
---
# git cat-file

கிட் களஞ்சிய பொருள்களுக்கான உள்ளடக்கம் அல்லது வகை மற்றும் அளவு தகவல்களை வழங்கவும்.
மேலும் தகவல்: <https://git-scm.com/docs/git-cat-file>.

- HEAD கமிட்டின் அளவை பைட்டுகளில் பெறுங்கள்:

`git cat-file -s HEAD`

- கொடுக்கப்பட்ட கிட் பொருளின் வகையை (குமிழ், மரம், கமிட், டேக்) பெறுங்கள்:

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- கொடுக்கப்பட்ட கிட் பொருளின் உள்ளடக்கத்தை அதன் வகையின் அடிப்படையில் அழகாக அச்சிடுக:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
