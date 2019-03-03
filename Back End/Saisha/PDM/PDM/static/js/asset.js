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

function openDetails(id1){
    clear();
    document.getElementById("dets").style.display="block";
    editor("dets ", id1);
}

function openPreventive(id1){
    clear();
    editor("preventive ", id1);
    document.getElementById("preventive").style.display="block";
}

function openHistory(id1){
    clear();
    editor("history ", id1);
    document.getElementById("history").style.display="block";
}
function editor(idName,idName2){
    alert(idName2);
    var x = document.getElementsByClassName('table-content');
    console.log(x.length);
    for (var i=0;i<x.length; i++){
        document.getElementsByClassName('row1')[i].innerHTML = idName + idName2; //get from db
        document.getElementsByClassName('row2')[i].innerHTML = idName + idName2;//get from db
        document.getElementsByClassName('row3')[i].innerHTML = idName + idName2;//get from db
        document.getElementsByClassName('row4')[i].innerHTML = idName + idName2;//get from db
        document.getElementsByClassName('row5')[i].innerHTML = idName + idName2;//get from db
        document.getElementsByClassName('row6')[i].innerHTML = idName + idName2;//get from db
    }
}