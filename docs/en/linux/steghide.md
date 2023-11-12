---
layout: page
title: linux/steghide (English)
description: "Steganography tool for JPEG, BMP, WAV and AU file formats."
content_hash: 5c46ab925229b47b5ff43330a39bd91a7468b5d8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# steghide

Steganography tool for JPEG, BMP, WAV and AU file formats.
More information: <https://github.com/StefanoDeVuono/steghide>.

- Embed data in a PNG, prompting for a passphrase:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data.txt</span>

- Extract data from a WAV audio file:

`steghide extract --stegofile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sound.wav</span>

- Display file information, trying to detect an embedded file:

`steghide info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Embed data in a JPEG image, using maximum compression:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data.txt</span>` --compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>

- Get the list of supported encryption algorithms and modes:

`steghide encinfo`

- Embed encrypted data in a JPEG image, e.g. with Blowfish in CBC mode:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data.txt</span>` --encryption `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blowfish|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cbc|...</span>
