// import express JS module into app 
// and creates its variable. 
var express = require('express'); 
var app = express(); 
var app4=express();

// Creates a server which runs on port 3000 and  
// can be accessed through localhost:3000 
app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app.get('', callName1); 
  
function callName1(req, res) { 
      
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python3',["./Mainmodule.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       /*var temp=''
        for(var i=0;i<splitString.length;i++)
        {
            var temp2=splitString[i].split("&");
            for(var j=0;j<temp2.length;j++)
            {
                temp=temp+temp2[j]+'<br>' 
            }
            temp=temp+splitString[i]+'<br>'
        }*/
        final='<b>----------------------------------------------------------------</b><br>';
        for (var i=0;i<splitString.length;i++)
        {
            temp=splitString[i].split('&');
            final=final+'<b>'+temp[0]+'</b>';
            for (var j=1;j< temp.length;j++)
            {
                final=final+'<br>'+temp[j];
            }
            final=final+'<br><b>----------------------------------------------------------------</b></br>';
        }
        


        res.send('<html><body>'+final+'</body></html>')
        //res.send('<html><head><script type="text/javascript">function myclick(){alert("Most popular product in the locality: '+splitString[0]+'product preffered by the same age group '+splitString[1]+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        //res.send(""); 
 
    } ) 
} 

  








app4.listen(8080, function() { 
    console.log('server running on port 8080'); 
} ) 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app4.get('', callName); 
  
function callName(req, res) { 
      
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python',["./viewallnotification.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       
        final='<b>----------------------------------------------------------------</b><br>';
        for (var i=0;i<splitString.length;i++)
        {
            temp=splitString[i].split('&');
            
            for (var j=0;j< temp.length;j++)
            {
                final=final+'<br>'+temp[j];
            }
            final=final+'<br><b>----------------------------------------------------------------</b></br>';
        }


        res.send('<html><body>'+final+'</body></html>')
        //res.send('<html><head><script type="text/javascript">function myclick(){alert("Most popular product in the locality: '+splitString[0]+'product preffered by the same age group '+splitString[1]+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        //res.send(""); 
 
    } ) 
} 


