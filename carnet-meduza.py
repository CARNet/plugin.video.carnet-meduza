<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.carnet-meduza" name="CARNet Meduza" version="1.0.0" provider-name="CARNet">
  <requires>
    <import addon="xbmc.python" version="2.19.0"/>
    <import addon="script.module.requests" version="2.12.4"/>
  </requires>
  <extension point="xbmc.python.pluginsource" library="carnet-meduza.py">
    <provides>video</provides>
  </extension>
  <extension point="xbmc.addon.metadata">
    <summary lang="en_gb">CARNet's VoD and live stream service for Croatian academic community</summary>
    <description lang="en_gb">
    CARNet Meduza is a service for the distribution of multimedia content designed for educational and academic institutions and the individual users of the CARNet member institutions.   The name of the system, Meduza, comes from the Greek word medomai () = "to plan", "to have an idea", "to find". It was chosen to emphasise the efficiency of the future platform. The desired objective of the CARNet Meduza is its availability to CARNet users as a source of knowledge, information and educational vido content.
    </description>
    <disclaimer lang="en_gb"></disclaimer>
    <language>hr</language>
    <platform>all</platform>
    <license>GNU GENERAL PUBLIC LICENSE. Version 2, June 1991</license>
    <forum></forum>
    <website></website>
    <email>iptv@carnet.hr</email>
    <source>https://github.com/scavara/plugin.video.carnet-meduza</source>
    <news></news>
    <assets>
        <icon>resources/icon.png</icon>
        <fanart>resources/fanart.jpg</fanart>
        <screenshot></screenshot>
    </assets>
  </extension>
</addon>
