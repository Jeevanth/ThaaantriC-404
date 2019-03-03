// import express JS module into app 
// and creates its variable. 
var express = require('express'); 
var app1 = express(); 
var app2 = express();
var app3=express();
var app4=express();

app1.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app1.get('', callName1); 
  
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
    var process = spawn('python',["./Mainmodule.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       
        


        res.send('<html><head><script type="text/javascript">function myclick(){alert("Most popular product in the locality: '+splitString[0]+'product preffered by the same age group '+splitString[1]+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
        //res.send('<html><head><script type="text/javascript">function myclick(){alert("Most popular product in the locality: '+splitString[0]+'product preffered by the same age group '+splitString[1]+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        //res.send(""); 
 
    } ) 
} 




app2.listen(3001, function() { 
    console.log('server running on port 3001'); 
} ) 
  

app2.get('', callName2); 
  
function callName2(req, res) { 
      
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
    var process = spawn('python',["./Mainmodule.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       
        

        res.send('<html><head><script type="text/javascript">function myclick(){alert("User based product prediction : '+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        

       // res.send('<html><head><script type="text/javascript">function myclick(){alert("User based product prediction : '+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
 
    } ) 
} 









app3.listen(3002, function() { 
    console.log('server running on port 3002'); 
} ) 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app3.get('', callName3); 
  
function callName3(req, res) { 
      
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
    var process = spawn('python',["./Mainmodule.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       
        


        res.send('<html><head><script type="text/javascript">function myclick(){alert("User basket analysis : '+splitString[4]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
        //res.send('<html><head><script type="text/javascript">function myclick(){alert("User based product prediction : '+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
 
    } ) 
} 


  






app4.listen(3003, function() { 
    console.log('server running on port 3003'); 
} ) 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app4.get('', callName4); 
  
function callName4(req, res) { 
      
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
    var process = spawn('python',["./Mainmodule.py" 
                            ] ); 
  //data="manthan"
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
   

 

    process.stdout.on('data', function(data) {
		data=data.toString(); 
        var splitString =data.split("$");
       
        


        res.send('<html><head><script type="text/javascript">function myclick(){alert("User time slots : '+splitString[8]+" "+splitString[7]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
       // res.send('<html><head><script type="text/javascript">function myclick(){alert("User based product prediction : '+splitString[2]+splitString[3]+'")}</script></head><body onload=myclick()><button onClick=myclick()>click</button></body></html>'); 
        
 
    } ) 
} 








