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

function HTTPUtils()
{
  this.sendViaPOST=function(httpReq,url,jsonMsg,callback){
    console.log("Try to Send JSON Req");
	httpReq.onreadystatechange=callback;
	httpReq.open("POST",url,true);
	httpReq.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	httpReq.send("jsonMsg="+jsonMsg);
  }
  
  this.sendViaGET=function(httpReq,url,jsonMsg,callback){
    console.log("Try to Send JSON Req");
	httpReq.onreadystatechange=callback;
	httpReq.open("GET",url+'/?jsonmsg='+jsonMsg+'&',true);
	//httpReq.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	httpReq.send(null);
  }
  
  this.CreateHttpObject=function(){
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
}