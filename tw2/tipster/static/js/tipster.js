function setupTipster(selector, tips, stopTipsURL) {
        $(document).ready( function() {
                if ( window._tipster === undefined ) { window._tipster = {}; }
                if ( window._tipster[selector] === undefined ) {
                        window._tipster[selector] = {};
                }
                window._tipster[selector]['tips'] = tips;
                window._tipster[selector]['stopTipsURL'] = stopTipsURL;
                window._tipster[selector]['i'] = Math.floor(
                        Math.random()*tips.length);

                nextTip(selector);

        });
}
function closeTip(selector) {
        $('#'+selector).slideUp('slow');
}
function stopTips(selector) {
        closeTip(selector);
        $.getJSON(window._tipster[selector]['stopTipsURL']);
}
function nextTip(selector) {
        window._tipster[selector]['i'] += 1;
        var i = window._tipster[selector]['i'] %= window._tipster[selector]['tips'].length;

        var stopTipsURL = window._tipster[selector]['stopTipsURL'];
        var content = window._tipster[selector]['tips'][i];

        var controls = '<div class="tipster_controls">';
        if ( stopTipsURL ) {
                controls += '<a href="javascript:stopTips(\'' + selector.replace(/:/g, '\\:') + '\');">(don\'t show me tips)</a>&nbsp;';
        }
        controls += '<a href="javascript:closeTip(\'' + selector.replace(/:/g, '\\:') + '\');">(close tip)</a>&nbsp;';
        controls += '<a href="javascript:nextTip(\'' + selector.replace(/:/g, '\\:') + '\');">(next tip)</a>&nbsp;';
        controls += '</div>';


        var span = '<span class="ui-icon ui-icon-info" style="float: left; margin-left: .3em; margin-right: .3em;"></span>';
        $('#'+selector).html('<div class="tipster_content">' + span + '<strong>Tip:</strong> ' + content + '</div>' + controls);
}
