/*
 * JS Classes for image distribution service
 */
var api;

function init(){
  console.log("initialzing ImageServiceAPI");
  api=new ImageServiceAPI();
  localinit();
}

function ImageServiceAPI(){
  this.messageFactory = new JSONMessageFactory();
  //this.messageHandler = new JSONMessageHandler();
  
  this.request=function(op){
    //console.log("send json to backend "+op+" data structure ");
    
    jsonMessage = this.messageFactory.createRequestMessage(op,OPSDATA[op]);
    messageHandler = new JSONMessageHandler();
    messageHandler.request( jsonMessage , op );
  };
  
  this.status=function(){
    console.log("status - get status from backend");
  };
}

function JSONMessageFactory(){
  this.createRequestMessage = function(operation,opData){
    
    jsonData = JSON.stringify(opData);
    return '{"op":"'+operation+'","deployments":'+jsonData+'}';
  };
}

function JSONMessageHandler(){
  httpReq={};
  httpUtils = new HTTPUtils();
  operation='';
  
  this.request=function(jsonMessage,op){
    opurl = OPSURL[op];
    //console.log("create request to backend with json data Model at url "+jsonMessage+" "+opurl);
    
    httpReq = httpUtils.CreateHttpObject();
    operation=op;
    //this.httpReq=httpReq;  
    //console.log("POST JSON Request");
    httpUtils.sendViaPOST(httpReq,opurl,jsonMessage,this.callback);
  };
  
  this.callback=function(data){
    //data.srcElement;
    if(httpReq.readyState==4){
		var objtabdata=httpReq.responseText;
		//console.log("post done "+objtabdata);
		//support for each message type here or use classes
		//console.log("op is or "+operation);
		view_id=OPSVIEW[operation];
		//console.log("div id "+view_id.div);
		document.getElementById(view_id.div).innerHTML="'"+operation+ "' Operation Completed";
		OPS_CB[operation](objtabdata);
	}
    
  }
}

