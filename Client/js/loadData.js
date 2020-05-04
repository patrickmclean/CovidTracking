function loadData() {
    // Loads country data through service call

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // parse the response for the number of available phrases
            // and highest (max) phrase number (there may be empty rows)
            var parser = new DOMParser();
            // change this next section to json

            var jsonDoc = parser.parseFromString(this.responseText, "text/json");
            document.getElementById("datasection").innerHTML = jsonDoc;
        }
    };
    xmlhttp.open("GET", "http://0.0.0.0:8080/getdata?country=netherlands", true);
    xmlhttp.send();
}
