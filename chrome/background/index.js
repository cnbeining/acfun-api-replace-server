chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        console.log(details.url);
        if (details.url.match("http://cdn.aixifan.com/player/sslhomura/AcNewPlayer151029.swf")) {
            var url = details.url.replace(
                    "http://cdn.aixifan.com/player/sslhomura/AcNewPlayer151029.swf",
                    "https://acfun-api.cnbeining.com/static/AcNewPlayer151029.swf");
            return {redirectUrl: url};
        }
        if (details.url.match("http://www.acfun.tv/video/getVideo.aspx?")) {
            var url = details.url.replace(
                    "http://www.acfun.tv/video/getVideo.aspx?",
                    "https://acfun-api.cnbeining.com/getVideo?");
            return {redirectUrl: url};
        }
        if (details.url.match("http://www.acfun.tv/video/createVideo.aspx?")) {
            var url = details.url.replace(
                    "zhuzhan",
                    "letv");
            return {redirectUrl: url};
        }
    },
    {urls:["http://cdn.aixifan.com/player/sslhomura/AcNewPlayer151029.swf*", "http://www.acfun.tv/video/getVideo.aspx?*", "http://www.acfun.tv/video/createVideo.aspx?*"]},
    ["blocking"]
);
