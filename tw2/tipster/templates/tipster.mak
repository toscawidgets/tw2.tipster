<%namespace name="tw" module="tw2.core.mako_util"/>
<div class="ui-widget">
<div ${tw.attrs(attrs=w.attrs)} class="ui-state-highlight ui-corner-all"></div>
<script type="text/javascript">
setupTipster('${w.selector}', ${w._tips}, '${w.stopTipsURL}');
</script>
</div>
