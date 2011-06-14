from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest

import tw2.tipster
import tw2.tipster.samples

class TestMenuWidget(WidgetTest):
    widget = tw2.tipster.TipsterWidget
    attrs = { 'id' : 'foo' }
    params = {
        'tips' : [
            'Test all your code.',
            'No, really.',
        ]
    }
    expected = """
<div class="ui-widget">
<div id="foo" class="ui-state-highlight ui-corner-all"></div>
<script type="text/javascript">
setupTipster('foo', ["Test all your code.", "No, really."], '');
</script>
</div>
"""

class TestDemoWidget(WidgetTest):
    widget = tw2.tipster.samples.DemoTipsterWidget
    attrs = { 'id' : 'foo' }
    params = {}
    expected = """
<div class="ui-widget">
<div id="foo" class="ui-state-highlight ui-corner-all"></div>
<script type="text/javascript">
setupTipster('foo', ["Here's a tip:  Wash your face!", "No really, wash your face!", "You know... if you specify a stopTipsURL you can stop tips.", "blah"], 'this-url-doesnot-exist____you-are-responsible-for-backend');
</script>
</div>
"""
