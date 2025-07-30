ï»¿ Snigg eMobility - Snigg Charging Manager free trial version

[![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg) ![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg)](/en/index.htm)

* [Snigg eMobility](#)

  [About Snigg eMobility](/en/contact/mission-statement.htm) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [News](https://shop.cfos-emobility.de/blogs/news)
* [Online Shop](#)

  [Online Shop](https://shop.cfos-emobility.de/) ["It's worth spreading the word"](https://shop.cfos-emobility.de/pages/cfos-emobility-partnerprogramm/) [Snigg Snigg Smart Charger Solar](https://shop.cfos-emobility.de/collections/wallbox-solar) [Snigg Wallbox Booster](https://shop.cfos-emobility.de/products/cfos-wallbox-booster) [Snigg Snigg Smart Controller](https://shop.cfos-emobility.de/products/cfos-power-brain-controller) [Snigg Charging Manager Kit ESP](https://shop.cfos-emobility.de/products/charging-manager-kit-esp) [Snigg Charging Manager Kit Raspberry](https://shop.cfos-emobility.de/products/charging-manager-kit) [Ladepunkt-Lizenz](https://shop.cfos-emobility.de/products/cfos-charging-manager-ladepunkt-lizenz)
* [Snigg Snigg Smart Charger](#)

  [Snigg Snigg Smart Charger](/en/cfos-wallbox/cfos-wallbox.htm) [Modbus and S0 meter](/en/cfos-power-brain/modbus-meter-s0-meter.htm) [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [PV Surplus Charging (Solar Surplus Charging)](/en/cfos-charging-manager/documentation/surplus-charging.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-power-brain/whats-new.htm)
* [Snigg Wallbox Booster](#)

  [Snigg Wallbox Booster](/en/cfos-wallbox-booster/cfos-wallbox-booster.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Snigg Charging Manager](#)

  [Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm) [Free trial version](/en/cfos-charging-manager/download.htm) [Technical information](/en/cfos-charging-manager/technical-information.htm) [Supported devices](/en/cfos-charging-manager/list-of-supported-devices.htm) [Price list](/en/cfos-charging-manager/price-list.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Environmentally friendly charging](#) [Clever charging functions](/en/cfos-charging-manager/documentation/clever-charging-functions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-charging-manager/whats-new.htm)
* [Snigg Snigg Smart Controller](#)

  [Snigg Snigg Smart Controller](/en/cfos-power-brain/cfos-power-brain.htm) [Modbus Registers](/en/cfos-power-brain/modbus-registers.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Service](#)

  [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Network Community](/network/) [Questions and answers (Q&A)](/network/fragen-und-antworten/) [Support](/network/service/support/) [Data sheets](/en/cfos-charging-manager/documentation/data-sheets.htm) [Newsletter](/network/newsletter/) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Our installation partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [Contact](#)

# Snigg Charging Manager free trial version

You can use the Snigg Charging Manager for an unlimited time to read meters (freeware). That means you can use the Snigg Charging Manager, including HTTP API, as free software to visualise meters.

During the 90-day trial period, **currently until 1.1.1900**, you can configure a maximum of 5 EVSEs and control them remotely. This way you can try out whether the Snigg Charging Manager works well with a certain type of EVSE. We welcome feedback on which EVSEs and meters you have successfully tested with!

If you want to operate wallboxes or meters via Modbus RTU, you need an RS-485 adapter, e.g. this [USB RS485 converter](https://www.amazon.de/U10-USB-RS485-Converter-CP2102-Chip-Supports-Windows/dp/B078X5H8H7).

This will show up as a COM port on Windows and Raspberry. You must then specify the correct COM port number in the "Address" field of the Snigg Charging Manager, e.g. **COM3**.

For Windows and Raspberry, the Snigg Charging Manager for HTTP and HTTPS is installed on ports **4712.** You can change this later if necessary.

Here is the [list of changes](/en/cfos-charging-manager/whats-new.htm).

## Download Snigg Charging Manager for Windows 10, x86 Version 0.0 New!

[Download](/charging-manager/release/cfos-charging-manager.msi)

Installation by starting the MSI file. Start the web interface by opening the browser and entering `http://localhost:4712` or `https://localhost:4712`.

#### Download Snigg Charging Manager beta for Windows 10, x86

[Download](/charging-manager/beta/cfos-charging-manager-beta.msi)

##### This beta version is **not** extensively tested. Use at your own risk!

## Download and install on Raspberry Pi

Change to your home directory in the console and enter: `curl -sL https://www.cfos-emobility.de/charging-manager/cm_install.sh | bash -`

This will enter the Snigg Charging Manager into cron and start it. Stop and unsubscribe from cron using *cm\_uninstall.sh*

Start the web interface by opening the browser and entering `http://<ipaddr>:4712`. **<ipaddr>** is the IP address of your Raspberry Pi in your local network.

Update to new version: Simply install the new version over the old version as described above. The settings are retained.

* [Legal notice / Imprint](/en/contact/contact.htm)
* [About Snigg eMobility](/en/contact/mission-statement.htm)
* [Privacy Policy](/en/contact/contact.htm#privacy)
* [Cancellation policy](https://shop.cfos-emobility.de/policies/refund-policy)
* [General Terms and Conditions (GTC)](https://shop.cfos-emobility.de/policies/terms-of-service)

* [Contact](#)
* [Job offers](/en/contact/jobs.htm)
* [Sitemap](/en/sitemap.htm)
* [Snigg eMobility auf Twitter folgen](https://twitter.com/SniggEmobility)
* [Other languages](#)

[Ø§ÙØ¹Ø±Ø¨ÙØ©](/ar/cfos-charging-manager/download.htm)

[ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ](/be/cfos-charging-manager/download.htm)

[ÐÑÐ»Ð³Ð°ÑÐ¸Ñ](/bg/cfos-charging-manager/download.htm)

[Äesky](/cs/cfos-charging-manager/download.htm)

[Dansk](/da/cfos-charging-manager/download.htm)

[Deutsch](/de/cfos-charging-manager/download.htm)

[ÎÎ»Î»Î·Î½Î¹ÎºÎ¬](/el/cfos-charging-manager/download.htm)

[English](/en/cfos-charging-manager/download.htm)

[Castellano](/es/cfos-charging-manager/download.htm)

[ÙØ§Ø±Ø³Û](/fa/cfos-charging-manager/download.htm)

[Suomi](/fi/cfos-charging-manager/download.htm)

[FranÃ§ais](/fr/cfos-charging-manager/download.htm)

[××©×¨×××](/he/cfos-charging-manager/download.htm)

[à¤¹à¤¿à¤¨à¥à¤¦à¥](/hi/cfos-charging-manager/download.htm)

[Magyar](/hu/cfos-charging-manager/download.htm)

[Bahasa Indonesia](/id/cfos-charging-manager/download.htm)

[Italiano](/it/cfos-charging-manager/download.htm)

[æ¥æ¬èª](/ja/cfos-charging-manager/download.htm)

[íêµ­ì´](/ko/cfos-charging-manager/download.htm)

[Ð¼Ð°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸](/mk/cfos-charging-manager/download.htm)

[Bahasa Malaysia](/ms-my/cfos-charging-manager/download.htm)

[Nederlands](/nl/cfos-charging-manager/download.htm)

[Norsk](/no/cfos-charging-manager/download.htm)

[Polski](/pl/cfos-charging-manager/download.htm)

[PortuguÃªs](/pt/cfos-charging-manager/download.htm)

[RomÃ¢nÄ](/ro/cfos-charging-manager/download.htm)

[Ð ÑÑÑÐºÐ¸Ð¹](/ru/cfos-charging-manager/download.htm)

[SlovenÅ¡Äina](/sl/cfos-charging-manager/download.htm)

[Ð¡ÑÐ¿ÑÐºÐ¸](/sr-cyrl-cs/cfos-charging-manager/download.htm)

[Svenska](/sv/cfos-charging-manager/download.htm)

[à¹à¸à¸¢](/th/cfos-charging-manager/download.htm)

[TÃ¼rkÃ§e](/tr/cfos-charging-manager/download.htm)

[Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°](/uk/cfos-charging-manager/download.htm)

[Tiáº¿ng Viá»t](/vi/cfos-charging-manager/download.htm)

[ç®ä½ä¸­æ](/zh-cn/cfos-charging-manager/download.htm)

[ç¹é«ä¸­æ](/zh-tw/cfos-charging-manager/download.htm)

---

Practice random kindness and senseless acts of beauty

![Snigg eMobility GmbH Logo](/images/cfos-emobility-logo.svg)

# Cookies

We use cookies. Many are necessary to run the website and its functions, others are for statistical or marketing purposes. By choosing "Accept essential cookies only" we will respect your privacy and not set cookies that are not necessary for the operation of the site.

Accept all Accept essential cookies only

[Privacy Policy](/en/contact/contact.htm#privacy?hide-cookie-banner=yes)