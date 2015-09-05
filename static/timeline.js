$(function() {
    var API_URL = "/api/timeline";
    var reload_button = $(".reload_button");
    var more_button = $(".more_button");
    var loading_bar = $(".loading_bar");
    var timeline = $(".timeline");

    var state = {
        is_loading: false,
tweets: []
    }

    var main = function() {
        init();
        fetch();
        more_button.click(onClickMore);
        reload_button.click(onClickReload);
    };

    var onClickReload = function() {
        init();
        fetch();
    };
    var onClickMore = function() {
        max_id = state.tweets[state.tweets.length -1].id_str;
        state.tweets.pop();
        fetch(max_id);
    };
    var stateChanged = function() {
        if (state.is_loading) {
            loading_bar.show();
        } else {
            loading_bar.hide();
        }
        build();
    };

    var init = function() {
        state.is_loading = true;
        state.tweets = [];
        stateChanged();
    };

    var fetch = function(max_id) { 
        $.getJSON(API_URL, {max_id: max_id}, callback);
    }

    var callback = function(data) {
        state.tweets = state.tweets.concat(data.tweets);
        state.is_loading = false;
        stateChanged();
    };

    var build = function() {
        tws = state.tweets;
        html = "";
        for(var i=0; i<tws.length; i++) {
            html += buildTweet(tws[i]); 
        }
        timeline.html(html);
    };

    var buildTweet = function(tweet) {
        var tweet_id = tweet.id_str;
        var tweet_body = tomorinize(tweet.text);
        var screen_name = tweet.user.screen_name; 
        var profile_icon = tweet.user.profile_image_url;
        var link = "https://twitter.com/" + screen_name + "/status/" + tweet_id;
        var outer = $("<div></div>").addClass("list-group-item");
        var media = $("<div></div>").addClass("media");
        var left = $("<div></div>").addClass("media-left");
        var icon = $("<image/>").addClass("tweet_icon media-object").attr("src", profile_icon);
        var body = $("<div></div>").addClass("media-body");
        var author = $("<div></div>");
        var user = $("<b></b>").addClass("tweet_user").text("友利奈緒");
        var uid = '&nbsp;<small><a href="' +
            link +
            '" class="tweet_link">@' +
            screen_name +
            '</a></small>';
        var content = $("<div></div>").addClass("tweet").text(tweet_body);

        author.append(user).append(uid);
        body.append(author).append(content);
        left.append(icon);
        media.append(left).append(body);
        outer.append(media);
        return outer[0].outerHTML;
    };

    var tomorinize = function(text) {
        return text.replace(/\@\S+/g, "@友利奈緒");
    };
    main();
});
