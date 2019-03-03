var http = require("http");
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true });
var fs = require("fs");
// Running Server Details.
var server = app.listen(8082, function () {
  var host = server.address().address
  var port = server.address().port
  console.log("Example app listening at %s:%s Port", host, port)
});
 
 
app.get('/', function (req, res) {
  var html='';
  //html+='<script>function onclick(){var e = document.getElementById("ddlViewBy");var strUser = e.options[e.selectedIndex].value;alert(strUser)}</script>';
  html +="<body>";
  html += "<form action='/thank'  method='post' name='form1'>";
  html += "Userid:</p><input type= 'number' name='userid'><br>";
  html += "Age:</p><input type='number' name='age'><br>";
  html += "Region:<br><input type='number' name='region'><br>";
  html += "<br><input type='submit' value='submit'>";
  html += "<INPUT type='reset'  value='reset'>";
  html += "</form>";
  html += "</body>";
  res.send(html);
});
 
app.post('/thank', urlencodedParser, function (req, res){
  var reply='';
  reply += "Your name is" + req.body.userid;
  reply += "Your E-mail id is" + req.body.age; 
  reply += "Your address is" + req.body.region;
  

  res.send(reply);
 
  var sampleObject = {
  userid: req.body.userid,
  userage: req.body.age,
  userregion:  req.body.region
};

fs.writeFile("./userresponce.json", JSON.stringify(sampleObject), (err) => {
  if (err) {
     alert(err);
      return;
  };
  
});
  
 });


 