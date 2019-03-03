function myFunction(){
    document.getElementById("myDIV").style.display="block";
    document.getElementById("tab").style.display="block";
}

function clear() {
  var i;
  var x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
}

function openDetails(){
    clear();
    document.getElementById("dets").style.display="block";
}

function openPreventive(){
    clear();
    document.getElementById("preventive").style.display="block";
}

function openHistory(){
    clear();
    document.getElementById("history").style.display="block";
}