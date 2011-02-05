from tw2.core.resources import encoder
import tw2.core as twc

import tw2.jquery
import tw2.jquery.base as tw2_jq_c_b
import tw2.jqplugins.ui.base as tw2_jq_ui

import formencode.validators as fv
import base

_pager_defaults = {'enableSearch': True, 'enableClear': True, 'gridModel': True}


class TipsterWidget(tw2_jq_ui.JQueryUIWidget):
    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
        base.tipster_js, base.tipster_css
    ]
    template = "mako:tw2.tipster.templates.tipster"

    tips = twc.Param(
        "A list of tips.", default=["Here's a tip.  Wash your face!"])

    stopTipsURL = twc.Param(
        "URL to stop tips from showing up for this user.", default="")

    def prepare(self):
        self._tips = encoder.encode(self.tips)
        super(TipsterWidget, self).prepare()

