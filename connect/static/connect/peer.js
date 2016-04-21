
$(document).ready(function() {


    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

});

$(document).ready(function(){

    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

    var peer = new Peer(window.MY_ID,{ host: 'bitsline.herokuapp.com', port: 443, path: '/',debug:0});

    peer.on('error', function(err){

        if(err.type == 'unavailable-id'){
         
            alert("It Seems you have bits-line open in another window.Please close this window and use the existing one. ps: If this is the only open window please try refreshing the page.")

        }

        else if (err.type == "network" || err.type=="disconnected"){
            peer.disconnect()
            window.setTimeout(function(){
            if (peer.disconnected == true){
               peer.reconnect()
            }
            },500)

        }
        else if(err.type== 'peer-unavailable'){
             clearTimeout(window.CallTimeout)
             step2();

    $.ajax({
              "type": "POST",
              "url": '../missed-call/',
              "data": {'username':$('#callto-id').val()}  
          });
             alert('User is unavailable.Please try again later.')
        }
        else{

            //console.log('  type: '+ err.type+ 'msg: '+err.message );
            step2();
        }

    });


        function clearIncomingCallUI(){
            if(window.IncomingBootbox){
                window.IncomingBootbox.modal('hide')
                 window.IncomingBootbox = ""
            }
            document.getElementById("ringtone").pause()
           
        }

        function clearOutCallUI(){
           document.getElementById("dialtone").pause()
        }


        function executeCMDData(data){
            if (typeof data.cmd === "undefined"){
               return
            }
            else{
                    data = data.cmd
                    if (data == "__QUIT__"){
                        endCall(false)
                    }
                    else if (data == "__TIME_OUT__"){
                        $("#missed-list").prepend('<li><a href="#">'+window.existingConn.peer+'</a></li>')
                        nos = parseInt($("#missed-call-nos").text())
                        nos+=1
                        $("#missed-call-nos").text(nos)
                    }
            }
        }
    
        function endCall(send){
            clearTimeout(window.CallTimeout)
            if(window.existingCall && window.existingCall.open == false && window.existingConn){
              console.log(window.existingCall)
               window.existingConn.send({cmd:"__TIME_OUT__"}) 
            }
            $("#their-video").attr('src',"")
            clearIncomingCallUI()
            if (send && window.existingConn){

                window.existingConn.send({cmd:"__QUIT__"})
            }
            window.setTimeout(function(){

            if (peer.disconnected == true){
                peer.reconnect()
                }
            if(window.existingCall){
                 window.existingCall.close();
            }
            if(window.existingConn){
               window.existingConn.close() 
            }
           
            
            window.existingCall = ""
            window.existingConn = ""

            }, 1000)

            step2()
        }



        window.onbeforeunload = function() { 
            endCall(true)
            peer.destroy()
 
        }
    

        peer.on('open', function(){
          $('#my-id').text(peer.id);
        });



        peer.on('connection',function(connection){  
        

            connection.on('open',function(){
           
                connection.send({cmd:"ACK"})
                window.existingConn = connection
                

                connection.on('data',function(data){
                  executeCMDData(data)
                });
                
                connection.on('close',function(){
                clearIncomingCallUI()
                })
            
            });
        });



    peer.on('call', function(call){
      
        if(window.IncomingBootbox){
            return
        }

        $.ajax({
              type: "POST",
              url: '../get-user-name/',
              data: {'username':call.peer},
              success: function(data){
              incomingCallUI(call, data+' ('+call.peer+')')

              },
              error: function(){
                incomingCallUI(call, call.peer)
              }  
          });


    });


    function incomingCallUI(call, user){
      document.getElementById("ringtone").play()
      window.IncomingBootbox = bootbox.confirm("You have a call from "+user,function(response){
            
            if(response){
              call.answer(window.localStream);
              step3(call);
            }

            else{
               call.close()
               window.existingConn.send({cmd:"__QUIT__"})
            } 
            document.getElementById("ringtone").pause()
            window.IncomingBootbox = ""
        });
    }



    function makeCall(){

                // Initiate a call!
        if (peer.disconnected == true){
           peer.reconnect()
        }
        if( $('#callto-id').val() == window.MY_ID){
            alert('You cannot call yourself')
             $('#callto-id').val("")
            return
        }
        var conn = peer.connect($('#callto-id').val(), window.localStream, reliable=true); 
        var call = peer.call($('#callto-id').val(), window.localStream);
        document.getElementById("dialtone").play()

        window.CallTimeout = window.setTimeout(function(){
            clearOutCallUI()
            endCall(false)
        },60000)

        conn.on('error',function(error){
            //console.log(error)
        })

        conn.on('data',function(data){
            executeCMDData(data)
            
        })

        conn.on('open',function(){
            window.existingConn = conn         

        });
        conn.on('close',function(){
            clearIncomingCallUI()
        })



        step3(call);

    }
   
      

        



step1();
    function step1 () {
      navigator.getUserMedia({audio: true, video: $("#cbox-video-call").prop("checked")}, function(stream){

        $('#my-video').prop('src', URL.createObjectURL(stream));

        window.localStream = stream;
        step2();
      }, function(){ $('#step1-error').show(); });
    }

    




    function step2 () {
      $('#step1, #step3').hide();
      $('#step2').show();
      clearOutCallUI()
    }

    


    function step3 (call) {
      // Hang up on an existing call if present
      if (window.existingCall) {
        window.existingCall.close();
      }

      // Wait for stream on the call, then set peer video display
      call.on('stream', function(stream){
        clearTimeout(window.CallTimeout)
        clearOutCallUI()
        $('#their-video').prop('src', URL.createObjectURL(stream));
      });

      
      window.existingCall = call;
      $('#their-id').text(call.peer);
      $('#step1, #step2').hide();
      $('#step3').show();
        }




    //bindings
    $('#make-call').click(function(){
      makeCall()
      });

    $('#end-call').click(function(){
        endCall(true) //send __QUIT__ true
      });


    $("#cbox-video-call").change(function(event){
      step1()
   });

    $('#step1-retry').click(function(){
        $('#step1-error').hide();
        step1();
      });

$("#missed-call-btn").click(function (){
        $("#missed-call-nos").text(0)
    });
$("#missed-list").on('click','li a',function(event){
    $('#callto-id').val($(event.target).text())
    makeCall()
})


  })
