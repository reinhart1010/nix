---
layout: page
title: common/podman (தமிழ்)
description: "காய்கள், கொள்கலன்கள் மற்றும் படங்களுக்கான எளிய மேலாண்மை கருவி."
content_hash: 8e48299c37b1a8764e31c8fc5acfc74f68b23f83
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman

காய்கள், கொள்கலன்கள் மற்றும் படங்களுக்கான எளிய மேலாண்மை கருவி.
போட்மேன் ஒரு Docker-CLI ஒப்பிடக்கூடிய கட்டளை வரியை வழங்குகிறது. எளிமையாகச் சொன்னால்: `alias docker=podman`.
மேலும் விவரத்திற்கு: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- அனைத்து கொள்கலன்களையும் பட்டியலிடு (இரண்டும் இயங்கும் மற்றும் நிறுத்தப்பட்டது):

`podman ps --all`

- தனிப்பயன் பெயருடன் ஒரு படத்திலிருந்து ஒரு கொள்கலனை உருவாக்கவும்:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படம்</span>

- ஏற்கனவே உள்ள கொள்கலனைத் தொடங்கவும் அல்லது நிறுத்தவும்:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>

- பதிவேட்டில் இருந்து ஒரு படத்தை இழுக்கவும் (டாக்கர் ஹப்பிற்கு இயல்புநிலை):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படம்</span>

- ஏற்கனவே பதிவிறக்கம் செய்யப்பட்ட படங்களின் பட்டியலைக் காண்பி:

`podman images`

- ஏற்கனவே இயங்கும் கொள்கலனில் ஒரு ஷெல் திறக்கவும்:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- நிறுத்தப்பட்ட கொள்கலனை அகற்றவும்:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட கொள்கலன்களின் பதிவுகளைக் காண்பி மற்றும் பதிவு வெளியீட்டைப் பின்பற்றவும்:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_ஐடி</span>
