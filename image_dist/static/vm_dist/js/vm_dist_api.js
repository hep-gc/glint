var covHttpReq;

function rem_vm(){
    img_name = document.getElementById("dist_img_sel").value;
    site_name = document.getElementById("dist_site_sel").value;
    covHttpReq=GetXmlHttpObject();
    console.log("Try to Remove VM Image"+img_name+site_name);
	var url="/image_dist/removeimage/";
	covHttpReq.onreadystatechange=dist_vm_response;
	covHttpReq.open("POST",url,true);
	covHttpReq.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	covHttpReq.setRequestHeader("X-CSRFToken",document.getElementsByName("scrfmiddlewaretoken").value);
	covHttpReq.send("img_name="+img_name+"&site_name="+site_name);
}


function rem_vm_get(){
    img_name = document.getElementById("dist_img_sel").value;
    site_name = document.getElementById("dist_site_sel").value;
    covHttpReq=GetXmlHttpObject();
    console.log("Try to Dist VM Image"+img_name+site_name);
	var url="/image_dist/removeimage/"+img_name+"/"+site_name+"/";
	covHttpReq.onreadystatechange=rem_vm_response;
	covHttpReq.open("GET",url,true);
	covHttpReq.send(null);
}

function rem_vm_response(){
	if(covHttpReq.readyState==4){
		var objtabdata=covHttpReq.responseText;
		console.log("rem got back"+objtabdata);
		//location.reload(false);
	}
}

function dist_vm(){
    img_name = document.getElementById("dist_img_sel").value;
    site_name = document.getElementById("pot_dist_sites").value;
    covHttpReq=GetXmlHttpObject();
    console.log("Try to Dist VM Image"+img_name+site_name);
	var url="/image_dist/distimage/";
	covHttpReq.onreadystatechange=dist_vm_response;
	covHttpReq.open("POST",url,true);
	covHttpReq.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	covHttpReq.setRequestHeader("X-CSRFToken",document.getElementsByName("scrfmiddlewaretoken").value);
	covHttpReq.send("img_name="+img_name+"&site_name="+site_name);
}

function dist_vm_get(){
    img_name = document.getElementById("dist_img_sel").value;
    site_name = document.getElementById("pot_dist_sites").value;
    covHttpReq=GetXmlHttpObject();
    console.log("Try to Dist VM Image"+img_name+site_name);
	var url="/image_dist/distimage/"+img_name+"/"+site_name+"/";
	covHttpReq.onreadystatechange=dist_vm_response;
	covHttpReq.open("POST",url,true);
	covHttpReq.send(null);
}

function dist_vm_response(){
	if(covHttpReq.readyState==4){
		var objtabdata=covHttpReq.responseText;
		console.log("dist got back"+objtabdata);
		//location.reload(false);
	}
}

function GetXmlHttpObject()
{
	if (window.XMLHttpRequest)
	  {
	  // code for IE7+, Firefox, Chrome, Opera, Safari
	  return new XMLHttpRequest();
	  }
	if (window.ActiveXObject)
	  {
	  // code for IE6, IE5
	  return new ActiveXObject("Microsoft.XMLHTTP");
	  }
	return null;
}