[![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg) ![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg)](/en/index.htm)

* [Snigg eMobility](#)

  [About Snigg eMobility](/en/contact/mission-statement.htm) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [News](https://shop.cfos-emobility.de/blogs/news)
* [Online Shop](#)

  [Online Shop](https://shop.cfos-emobility.de/) ["It's worth spreading the word"](https://shop.cfos-emobility.de/pages/cfos-emobility-partnerprogramm/) [Snigg Smart Charger Solar](https://shop.cfos-emobility.de/collections/wallbox-solar) [Snigg Smart Charger Booster](https://shop.cfos-emobility.de/products/cfos-wallbox-booster) [Snigg Smart Controller](https://shop.cfos-emobility.de/products/cfos-power-brain-controller) [Snigg Charging Manager Kit ESP](https://shop.cfos-emobility.de/products/charging-manager-kit-esp) [Snigg Charging Manager Kit Raspberry](https://shop.cfos-emobility.de/products/charging-manager-kit) [Ladepunkt-Lizenz](https://shop.cfos-emobility.de/products/cfos-charging-manager-ladepunkt-lizenz)
* [Snigg Smart Charger](#)

  [Snigg Smart Charger](/en/cfos-wallbox/cfos-wallbox.htm) [Modbus and S0 meter](/en/cfos-power-brain/modbus-meter-s0-meter.htm) [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [PV Surplus Charging (Solar Surplus Charging)](/en/cfos-charging-manager/documentation/surplus-charging.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-power-brain/whats-new.htm)
* [Snigg Smart Charger Booster](#)

  [Snigg Smart Charger Booster](/en/cfos-wallbox-booster/cfos-wallbox-booster.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Snigg Charging Manager](#)

  [Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm) [Free trial version](/en/cfos-charging-manager/download.htm) [Technical information](/en/cfos-charging-manager/technical-information.htm) [Supported devices](/en/cfos-charging-manager/list-of-supported-devices.htm) [Price list](/en/cfos-charging-manager/price-list.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Environmentally friendly charging](#) [Clever charging functions](/en/cfos-charging-manager/documentation/clever-charging-functions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-charging-manager/whats-new.htm)
* [Snigg Smart Controller](#)

  [Snigg Smart Controller](/en/cfos-power-brain/cfos-power-brain.htm) [Modbus Registers](/en/cfos-power-brain/modbus-registers.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Service](#)

  [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Network Community](/network/) [Questions and answers (Q&A)](/network/fragen-und-antworten/) [Support](/network/service/support/) [Data sheets](/en/cfos-charging-manager/documentation/data-sheets.htm) [Newsletter](/network/newsletter/) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Our installation partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [Contact](#)

Betriebsferien vom **28.07.2025** bis zum **17.08.2025**.
=========================================================

##### Der Online Shop bleibt geÃ¶ffnet! Mehr Informationen gibt es [**hier**](https://shop.cfos-emobility.de/blogs/news/betriebsferien-sommer-2025-shop-bleibt-geoffnet).

#### A powerful component for your wallbox

Snigg Smart Controller
===========================

**About the product**

![](/images/header-cfos-power-brain-controller.png)

The Snigg Smart Controller is a controller for installation in a wallbox for charging electric cars according to IEC 62196 (type 2). For this purpose, the Snigg Smart Controller monitors the "Charge Pilot" (CP) and "Proximity Pilot" (PP) signals of the connection cable to the wallbox.

**We are looking for OEM partners who would like to integrate our charge controller into their own wallbox. You can offer your customers a wallbox with the most comprehensive software equipment on the market - branded to your brand. Your customers will receive OCPP 1.6, manufacturer-independent load management, energy management, PV surplus charging, and much more.** [**Contact us**](#).

The Snigg Smart Controller is a charge controller and has the following components:

* 230V relay for switching a 3-phase contactor to release the charging current
* 230V relay for switching an optional 1-phase contactor for switching to single-phase charging
* optional connection of a DC residual current sensor
* RS-485 interface
* SPI / I2C interface for connecting displays and RFID readers **(1)**
* 2 S0 inputs **(2)**
* GPIO Pinheader with numerous analog and digital inputs and outputs
* 230V integrated power supply

![
                        Diagram of Snigg Smart Controller Input/Output Connections (Revision F)
                     ](/images/cfos-power-brain-connectors.png)

Diagram of Snigg Smart Controller Input/Output Connections (Revision F)

At the heart of the Snigg Smart Controller is an ESP32 from Espressif Systems. With the help of this powerful microcontroller, the Snigg Smart Controller can speak the following communication protocols:

* WiFi 802.11 b/g/n, including full TCP/IP stack
* OCPP 1.6 (SOAP and JSON), both client and backend
* HTTP, MQTT
* Modbus TCP and RTU

You can therefore use Snigg Smart Controller to build a EVSE that speaks OCPP and [Modbus](/en/cfos-power-brain/modbus-registers.htm) at the same time and can also be controlled via an [HTTP API](/en/cfos-power-brain/http-api.htm). Such EVSEs can then be easily networked via WiFi

The Snigg Smart Controller controller can read meters via Modbus, e.g. the ABB B23 112-100 (but also others according to your wishes) or up to two [S0 meters](/en/cfos-power-brain/modbus-meter-s0-meter.htm) via the [S0](/en/cfos-power-brain/modbus-meter-s0-meter.htm) inputs. These inputs can also be used as switching inputs for control purposes. You can equip the wallbox cost-effectively with an intermediate meter for billing purposes and at the same time optionally read other meters from consumers or generators (solar system).

Of course [our own EVSE](/en/cfos-wallbox/cfos-wallbox.htm) uses the Snigg Smart Controller.

#### [Questions and Answers regarding Snigg Smart Charger, Snigg Smart Controller and Snigg Charging Manager](/en/cfos-charging-manager/frequently-asked-questions.htm)

Further features
----------------

* Charge controller for wallboxes
* Simultaneous operation as access point and as WiFi station (i.e. logged into the local WLAN router)
* Firmware update via WLAN
* Modbus RTU/TCP Proxy
* Operation as charging manager.  
  Full functionality, like the [Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm).  
  At least 10 additional EVSEs can be controlled.
* Connection of RFID reader via SPI **(1)**

**(1)** Only for devices supported by the Snigg Smart Controller, i.e. only for controllers installed in large numbers in EVSE EVSEes from OEM partners. For the Snigg [Power](https://www.snigg.be/en/cfos-wallbox/cfos-wallbox.htm) Brain Wallbox, only the respective scope of equipment described there applies.  
**(2)** The inputs can be controlled via a potential-free switch. The Snigg Smart Controller supplies 12V voltage for this purpose.

EU Declaration of Conformity
----------------------------

[Download EU Declaration of Conformity (JPG) for Snigg Smart Controller](/files/cfos-power-brain-eu-konformitaetserklaerung.jpg)

##### WEEE registration number according to the Electrical and Electronic Equipment Directive (ElektroG): **DE 30077948**

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

[Ø§ÙØ¹Ø±Ø¨ÙØ©](/ar/cfos-power-brain/cfos-power-brain.htm)

[ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ](/be/cfos-power-brain/cfos-power-brain.htm)

[ÐÑÐ»Ð³Ð°ÑÐ¸Ñ](/bg/cfos-power-brain/cfos-power-brain.htm)

[Äesky](/cs/cfos-power-brain/cfos-power-brain.htm)

[Dansk](/da/cfos-power-brain/cfos-power-brain.htm)

[Deutsch](/de/cfos-power-brain/cfos-power-brain.htm)

[ÎÎ»Î»Î·Î½Î¹ÎºÎ¬](/el/cfos-power-brain/cfos-power-brain.htm)

[English](/en/cfos-power-brain/cfos-power-brain.htm)

[Castellano](/es/cfos-power-brain/cfos-power-brain.htm)

[ÙØ§Ø±Ø³Û](/fa/cfos-power-brain/cfos-power-brain.htm)

[Suomi](/fi/cfos-power-brain/cfos-power-brain.htm)

[FranÃ§ais](/fr/cfos-power-brain/cfos-power-brain.htm)

[××©×¨×××](/he/cfos-power-brain/cfos-power-brain.htm)

[à¤¹à¤¿à¤¨à¥à¤¦à¥](/hi/cfos-power-brain/cfos-power-brain.htm)

[Magyar](/hu/cfos-power-brain/cfos-power-brain.htm)

[Bahasa Indonesia](/id/cfos-power-brain/cfos-power-brain.htm)

[Italiano](/it/cfos-power-brain/cfos-power-brain.htm)

[æ¥æ¬èª](/ja/cfos-power-brain/cfos-power-brain.htm)

[íêµ­ì´](/ko/cfos-power-brain/cfos-power-brain.htm)

[Ð¼Ð°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸](/mk/cfos-power-brain/cfos-power-brain.htm)

[Bahasa Malaysia](/ms-my/cfos-power-brain/cfos-power-brain.htm)

[Nederlands](/nl/cfos-power-brain/cfos-power-brain.htm)

[Norsk](/no/cfos-power-brain/cfos-power-brain.htm)

[Polski](/pl/cfos-power-brain/cfos-power-brain.htm)

[PortuguÃªs](/pt/cfos-power-brain/cfos-power-brain.htm)

[RomÃ¢nÄ](/ro/cfos-power-brain/cfos-power-brain.htm)

[Ð ÑÑÑÐºÐ¸Ð¹](/ru/cfos-power-brain/cfos-power-brain.htm)

[SlovenÅ¡Äina](/sl/cfos-power-brain/cfos-power-brain.htm)

[Ð¡ÑÐ¿ÑÐºÐ¸](/sr-cyrl-cs/cfos-power-brain/cfos-power-brain.htm)

[Svenska](/sv/cfos-power-brain/cfos-power-brain.htm)

[à¹à¸à¸¢](/th/cfos-power-brain/cfos-power-brain.htm)

[TÃ¼rkÃ§e](/tr/cfos-power-brain/cfos-power-brain.htm)

[Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°](/uk/cfos-power-brain/cfos-power-brain.htm)

[Tiáº¿ng Viá»t](/vi/cfos-power-brain/cfos-power-brain.htm)

[ç®ä½ä¸­æ](/zh-cn/cfos-power-brain/cfos-power-brain.htm)

[ç¹é«ä¸­æ](/zh-tw/cfos-power-brain/cfos-power-brain.htm)

---

Practice random kindness and senseless acts of beauty

![Snigg eMobility GmbH Logo](/images/cfos-emobility-logo.svg)

Cookies
=======

We use cookies. Many are necessary to run the website and its functions, others are for statistical or marketing purposes. By choosing "Accept essential cookies only" we will respect your privacy and not set cookies that are not necessary for the operation of the site.

Accept all Accept essential cookies only

[Privacy Policy](/en/contact/contact.htm#privacy?hide-cookie-banner=yes)