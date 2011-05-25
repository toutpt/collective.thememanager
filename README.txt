Introduction
============

This add-on add feature to the brand new plone.app.theming add-on.
It gives you a 'sourceslist' settings where you can add themes providers URLs
Once you have add themes providers, you can select a theme, it will be 
downloaded and installed for you.

This add-on add a dexterity content type 'Theme' to let you providing themes.

Select a remote theme
=====================

You can select a remote theme in a list of themes. The list is built from
the 'collective.thememanager.sourceslist' settings. This settings is a list
of url that is supposed to contains a json rendering of the themes provided

Be a themes provider
====================

To be a theme provider, you just have to add some 'Theme' contents in your website.
The url of the json service is 'http://www.mywebsite.com/@@themes_json'. It will list
all themes you have in your websites !

