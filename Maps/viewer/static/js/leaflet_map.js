window.NLIMaps = {};

$(document).ready(function(){
    NLIMaps.map = createMap();
});

/**
 *  get the position of the user
 */
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}


function createMap() {
    // set the map where the uer is (based on his coordinates
    var baseMap = L.map('map', { zoomControl:false }).setView(["31.771959", "35.217018"], 16);

    // Initialise the FeatureGroup to store editable layers
    var drawnItems = new L.FeatureGroup();
    baseMap.addLayer(drawnItems);

    // Initialise the draw control and pass it the FeatureGroup of editable layers
    var drawControl = new L.Control.Draw({
        position: 'topright',
        draw: {
            polyline: {
                metric: true
            },
            polygon: {
                allowIntersection: false,
                showArea: true,
                drawError: {
                    color: '#b00b00',
                    timeout: 1000
                },
                shapeOptions: {
                    color: '#bada55'
                }
            },
            circle: {
                shapeOptions: {
                    color: '#662d91'
                }
            },
            marker: false
        },
        edit: {
            featureGroup: drawnItems,
            remove: false
        }
    });
    baseMap.addControl(drawControl);

    // create a base map layer
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                    maxZoom: 18,
                    id: 'nirgn975.cigmtjxyw000rc3knz02njkhn',
                    accessToken: 'pk.eyJ1IjoibmlyZ245NzUiLCJhIjoiY2lnbXRqeTcxMDAwdmx6a3RueGViemV0eCJ9.3wBhw04dxzXHfd56yUfufQ'
    }).addTo(baseMap);

    baseMap.on('draw:created', function (e) {
        var type = e.layerType,
            layer = e.layer;

        if (type === 'marker') {
            layer.bindPopup('A popup!');
        }

        drawnItems.addLayer(layer);
        geoSearch(layer._latlngs);
    });

    baseMap.on('draw:edited', function (e) {
        var layers = e.layers;
        var countOfEditedLayers = 0;
        layers.eachLayer(function(layer) {
            countOfEditedLayers++;
        });
        console.log("Edited " + countOfEditedLayers + " layers");
    });
    return baseMap;
}


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function geoSearch(array) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    debugger;
    var csrftoken = getCookie('csrftoken');
    var lenlat = {
        "left-down": array[0],
        "left-up": array[1],
        "right-up": array[2],
        "right-down":array[3],
        };
    $.ajax({
            type: 'POST',
            url: '/getGeoThumbs/',
            data: "{}",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            //data: {'lenlat[]': lenlat},
        });

    // $.post("getThumbs/" + JSON.stringify())
    // .done(function(data){
    //     var thumbs =[];
    //     var thumbs_container = $("#thumb");
    //     $.each(data, function(key, thumb){
    //         debugger;
    //         thumbs.push(
    //             "<li class='thumbnail-click'><div class='demo-card-image mdl-card mdl-shadow--2dp' style='background: url("+ thumb.url +") center / cover;'>" +
    //             "<img src='"+thumb.url+"' data-id='"+thumb.id+"' style='visibility:hidden;'/>" +
    //             "<div class='mdl-card__actions'>" +
    //             "<span class='demo-card-image__filename'>" + thumb.title + "</span>" +
    //             "</div></div></li>");
    //     });
    // });
}
