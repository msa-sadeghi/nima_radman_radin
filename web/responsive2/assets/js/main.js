function my(){
    var e = document.getElementById("test");
    if (e.className === "nav"){
        e.className += " responsive";
    }
    else{
        e.className = "nav";
    }
}