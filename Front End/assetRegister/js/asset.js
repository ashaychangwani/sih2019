var idName2="test";
function openCity(cityName, clicked_id2) {
  var i;
    document.getElementById("dets").style.display="none";
    document.getElementById("preventive").style.display="none";
    document.getElementById("history").style.display="none";
  var x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
    
  document.getElementById(cityName).style.display = "block";
  idName2 = clicked_id2;
    alert(idName2 + cityName);
}

var idName, length; 
length = document.querySelectorAll('#history .table-row').length;
console.log(length);

function reply_click(clicked_id)
{
    alert(clicked_id);
    
    idName = clicked_id;
    console.log(idName);
    document.getElementById(idName).addEventListener("click", function(){
    for(var i = 0; i < length; i++){
        alert("test"+idName+idName2);
        document.getElementById("myDIV").style.display = "block";
        document.getElementsByClassName("row1")[i].innerHTML = "";
        document.getElementsByClassName("row1")[i].innerHTML = "London" + idName + idName2; //get from db
        document.getElementsByClassName("row2")[i].innerHTML = "";
        document.getElementsByClassName("row2")[i].innerHTML = "Paris" + idName + idName2;//get from db
        document.getElementsByClassName("row3")[i].innerHTML = "";
        document.getElementsByClassName("row3")[i].innerHTML = "Tokyo" + idName + idName2;//get from db
        document.getElementsByClassName("row4")[i].innerHTML = "";
        document.getElementsByClassName("row4")[i].innerHTML = "Tokyo" + idName + idName2;//get from db
        document.getElementsByClassName("row5")[i].innerHTML = "";
        document.getElementsByClassName("row5")[i].innerHTML = "Tokyo" + idName + idName2;//get from db
        document.getElementsByClassName("row6")[i].innerHTML = "";
        document.getElementsByClassName("row6")[i].innerHTML = "Tokyo" + idName + idName2;//get from db
    }
});

}