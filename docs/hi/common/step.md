---
layout: page
title: common/step (हिन्दी)
description: "सार्वजनिक कुंजी अवसंरचना (PKI) सिस्टम और कार्यप्रवाह बनाने, संचालित करने और स्वचालित करने के लिए एक उपयोग में आसान CLI उपकरण।"
content_hash: e686602f4dc8c5146c1b8e61a4758980dbe82198
last_modified_at: 2024-11-21
related_topics:
  - title: English version
    url: /en/common/step.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/step.html
    icon: bi bi-globe
tldri18n_status: 2
---
# step

सार्वजनिक कुंजी अवसंरचना (PKI) सिस्टम और कार्यप्रवाह बनाने, संचालित करने और स्वचालित करने के लिए एक उपयोग में आसान CLI उपकरण।
देखें: `openssl`।
अधिक जानकारी: <https://smallstep.com/docs/step-cli/>।

- एक प्रमाणपत्र की सामग्री का निरीक्षण करें:

`step certificate inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सर्टिफिकेट.crt/का/पथ</span>

- एक रूट CA प्रमाणपत्र और एक कुंजी बनाएँ (निजी कुंजी पासवर्ड सुरक्षा को छोड़ने के लिए `--no-password --insecure` जोड़ें):

`step certificate create "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उदाहरण Root CA</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट-सीए.crt/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रूट-ca.key/का/पथ</span>` --profile root-ca`

- एक विशिष्ट होस्टनाम के लिए एक प्रमाणपत्र उत्पन्न करें और इसे रूट CA के साथ हस्ताक्षरित करें (सरलीकरण के लिए CSR उत्पन्न करना छोड़ सकते हैं):

`step certificate create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.crt/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.key/का/पथ</span>` --profile leaf --ca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root-ca.crt/का/पथ</span>` --ca-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root-ca.key/का/पथ</span>

- एक प्रमाणपत्र श्रृंखला की पुष्टि करें:

`step certificate verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.crt/का/पथ</span>` --roots `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root-ca.crt/का/पथ</span>` --verbose`

- PEM फ़ॉर्मेट के प्रमाणपत्र को DER में परिवर्तित करें और इसे डिस्क पर लिखें:

`step certificate format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate.pem/का/पथ</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate.der/का/पथ</span>

- सिस्टम के डिफ़ॉल्ट ट्रस्ट स्टोर में एक रूट प्रमाणपत्र स्थापित करें या हटा दें:

`step certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root-ca.crt/का/पथ</span>

- एक RSA/EC निजी और सार्वजनिक कुंजी जोड़ी बनाएँ (निजी कुंजी पासवर्ड सुरक्षा को छोड़ने के लिए `--no-password --insecure` जोड़ें):

`step crypto keypair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सार्वजनिक/कुंजी/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निजी/कुंजी/का/पथ</span>` --kty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">RSA|EC</span>

- उप-कमांड के लिए सहायता दिखाएँ:

`step `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh</span>` --help`
