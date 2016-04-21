var fs = require('fs');
var PeerServer = require('peer').PeerServer;

var server = PeerServer({
  port: 9000,
  ssl: {
    key: fs.readFileSync('stunnel/stunnel.key'),
    cert: fs.readFileSync('stunnel/stunnel.cert')
  }
});

server.on('error',function(id){
	console.log(id)
})
server.on('connection',function(id){
	console.log(id)
})
server.on('disconnect',function(id){
	console.log(id)
})

console.log("Server started at 9000")
