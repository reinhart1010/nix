---
layout: page
title: common/podman (தமிழ்)
description: "காய்கள், கொள்கலன்கள் மற்றும் படங்களுக்கான எளிய மேலாண்மை கருவி."
content_hash: b16264ac40026f8d0e2680a192fed8582570a04a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Podman

காய்கள், கொள்கலன்கள் மற்றும் படங்களுக்கான எளிய மேலாண்மை கருவி.
போட்மேன் ஒரு Docker-CLI ஒப்பிடக்கூடிய கட்டளை வரியை வழங்குகிறது. எளிமையாகச் சொன்னால்: `alias docker=podman`.
மேலும் விவரத்திற்கு: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- கொள்கலன்கள் பற்றிய தகவலை அச்சிடவும்:

`podman ps`

- அனைத்து கொள்கலன்களையும் பட்டியலிடு (இரண்டும் இயங்கும் மற்றும் நிறுத்தப்பட்டது):

`podman ps --all`

- ஒன்று அல்லது அதற்கு மேற்பட்ட கொள்கலன்களைத் தொடங்கவும்:

`podman start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_ஐடி</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட இயங்கும் கொள்கலன்களை நிறுத்துங்கள்:

`podman stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_ஐடி</span>

- பதிவேட்டில் இருந்து ஒரு படத்தை இழுக்கவும் (டாக்கர் ஹப்பிற்கு இயல்புநிலை):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படத்தின்_பெயர்</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படத்தின்_டேக்</span>

- ஏற்கனவே இயங்கும் கொள்கலனில் ஒரு ஷெல் திறக்க:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட நிறுத்தப்பட்ட கொள்கலன்களை அகற்றவும்:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_ஐடி</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட கொள்கலன்களின் பதிவுகளைக் காண்பி மற்றும் பதிவு வெளியீட்டைப் பின்பற்றவும்:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_ஐடி</span>
