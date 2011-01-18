"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets

class DemoTipsterWidget(widgets.TipsterWidget):
    tips = [
        "Here's a tip:  Wash your face!",
        "No really, wash your face!",
        "You know... if you specify a stopTipsURL you can stop tips.",
        "blah",
    ]
    stopTipsURL = 'this-url-doesnot-exist____you-are-responsible-for-backend'
