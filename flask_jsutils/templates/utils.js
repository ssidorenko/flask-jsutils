{% autoescape false %}

var flask_util = function() {
    var rule_map = {{ rule_map }};

    function url_for(endpoint, params) {
        if (!params) {
            params = {};
        }

        if (!rule_map[endpoint]) {
            throw('endpoint does not exist: ' + endpoint);
        }

        var rule = rule_map[endpoint];

        var used_params = {};


        var rex = /\<\s*(\w+:)*(\w+)\s*\>/ig;

        var path = rule.replace(rex, function(_i, _0, _1) {
            if (params.hasOwnProperty(_1)) {
                used_params[_1] = params[_1];
                return encodeURIComponent(params[_1]);
            } else {
                throw(_1 + ' does not exist in params');
            }
        });

        var query_string = '';

        for(var k in params) {
            if (used_params.hasOwnProperty(k)) {
                continue;
            }

            var v = params[k];
            if(query_string.length > 0) {
                query_string += '&';
            }
            query_string += encodeURIComponent(k)+'='+encodeURIComponent(v);
        }

        var url = path;
        if (query_string.length > 0) {
            url += '?'+query_string;
        }

        return url;
    }

    return {
        url_for: url_for,
        rule_map: rule_map
    }
}();

{% endautoescape %}
