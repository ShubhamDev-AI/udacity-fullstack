
let $form = $('#form-container');

var NYT_API_KEY = "4fe5b013ba3f4a10b82f8c9e58404456";

function loadData() {

    var $body = $('body');
    var $greeting = $('#greeting');
    var $streetInput = $('#street');
    var $cityInput = $('#city');

    var city = $cityInput.val();
    var street = $streetInput.val();

    // load streetview
    setGoogleStreetviewImage(city, street);
    loadNYTArticles(city);
    loadWikiArticles(city, street);

    return false;
};

function setGoogleStreetviewImage(city, street){
    var $bgimg = $('#bgimg');
    var url = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + city + ',' + street;
    $bgimg.attr('src', url);
}

function loadNYTArticles(city){
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');

    $nytElem.text("");

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
        'api-key': NYT_API_KEY,
        'q': city
    });

    $.getJSON(url, function(data){
        console.log(data);
        data.response.docs.forEach((doc) => {
            var item = document.createElement('li');
            var a = document.createElement('a');
            item.className = 'article';
            a.href = doc.web_url;
            a.target = '_blank';
            a.innerHTML = doc.headline.main;
            item.appendChild(a);
            $nytElem.append(item);
        });
    })
    .fail(function(err){
        $nytElem.text("Oops! Failed to load articles.")
    });

}

function loadWikiArticles(city, street){
    var $wikiElem = $('#wikipedia-links');
    $wikiElem.text("");

    let url = 'https://en.wikipedia.org/w/api.php';

    url += '?' + $.param({
        'action': 'query',
        'format': 'json',
        'titles': city + '|' + street,
        'prop': 'links',
    });

    $.ajax(url, {
        dataType: "jsonp",
        success: function(data){
            console.log(data);

            let pages = data.query.pages;

            Object.keys(pages).map(key => {
                let page = pages[key];
                var item = document.createElement('li');
                var a = document.createElement('a');
                item.className = 'article';
                a.href = 'https://en.wikipedia.org/wiki/' + page.title;
                a.target = '_blank';
                a.innerHTML = page.title;
                item.appendChild(a);
                $wikiElem.append(item);
            });

        },
        fail: function(){
            $wikiElem.text("Oops! Failed to load articles.")
        }
    })

}

$form.submit(loadData);
