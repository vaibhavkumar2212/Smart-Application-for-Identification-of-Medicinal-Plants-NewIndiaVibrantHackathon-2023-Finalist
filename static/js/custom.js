toastr.options = {
    "closeButton": true,
    "debug": false,
    "positionClass": "toast-top-right",
    "onclick": null,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
};


// to get current year
function getYear() {
  var currentDate = new Date();
  var currentYear = currentDate.getFullYear();
  document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


const startButton = document.getElementById('start-button');
const outputText = document.getElementById('output-text');
const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
let silenceTimer;
const myList = [];

recognition.continuous = true;
recognition.interimResults = true;






// Handle item selection
$(".dropdown-item").on("click", function() {
  var selectedID = $(this).data("id");
  $("#selectedItemID").text(selectedID);
  var dataToSend = {'language':selectedID};
  $.ajax({
      type: 'POST',
      url: '/update_content',
      contentType: 'application/json',
      data: JSON.stringify(dataToSend),
      success: function(response) {

          toastr.success('Language: '+response.data.language_name);
          var data=response['data'];
          console.log(data)
          $('#home').html(data.home);
          $('#profile').html(data.profile);
          $('#about').html(data.about);
          $('#about_content').html(data.about_content);
          $('#about_head').html(data.about_head);
          $('#profile_content').html(data.profile_content);
          $('#dropdownMenuButton').html(data.lan);
          // Handle the response from the server here
      },
      error: function(error) {
        toastr.error('Cant translate');
      }
  });



});


// Show message overlay
    $("#show-message").click(function () {
        $("#overlay").fadeIn();
        $("#message-container").fadeIn();
    });

    // Hide message overlay
    $("#close-message").click(function () {
        $("#overlay").fadeOut();
        $("#message-container").fadeOut();
    });


startButton.addEventListener('click', () => {
      $('#search_text').val("");
      alert("Try Speaking");

      recognition.start();

      $('#exampleModal').modal('show');
      startButton.disabled = true;
      startButton.classList.remove('btn-primary');
      startButton.classList.add('btn-secondary');
            outputText.textContent = '';

      recognition.onresult = (event) => {
          const transcript = Array.from(event.results)
              .map((result) => result[0].transcript)
              .join(' ');

          outputText.textContent = transcript;
          myList.push(outputText.textContent);


          // Reset the silence timer
          clearTimeout(silenceTimer);
          silenceTimer = setTimeout(() => {
              recognition.stop();
              stopRecording();
          }, 10000); // Adjust the duration (in milliseconds) as needed
      };

recognition.onend = () => {
    alert("Record Stop");
    recognition.stop();
    stopRecording();
    const lastElement = myList.slice(-1)[0];
    var language_id= $('#dropdownMenuButton').text();
    console.log(language_id);
    if(language_id=='\n    ભાષા\n  '){
        language_id='gujrati'
    }
    if(language_id=='\n    Language\n  '){
        language_id='english'
    }
    if(language_id=='\n    भाषा\n  '){
        language_id='hindi'
    }
    console.log(language_id);
             



   var dataToSend = {'search': lastElement,'language':language_id};

    $.ajax({
        type: 'POST',
        url: '/translator',
        contentType: 'application/json',
        data: JSON.stringify(dataToSend),
        success: function(response) {
            console.log(response);
            // Handle the response from the server here
            var searchtext=response['plant_name']
            console.log(searchtext);
            var results=searchtext['data']
            console.log(results);
            $('#search_text').val(results['plant']);
        },
        error: function(error) {
            console.error(error);
            // Handle any errors here
        }
    });

    $('#exampleModal').modal('hide');

};
});

  

function stopRecording() {
    startButton.disabled = false;
    startButton.classList.remove('btn-secondary');
    startButton.classList.add('btn-primary');
}

function openCam(){
         $("#videoContainer").show();
         captureImage();
         
      }
let videoStream; // To store the video stream

        function captureImage() {
            const video = document.getElementById('video');
            const canvas = document.getElementById('canvas');
            const context = canvas.getContext('2d');

            // Get user's camera
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    videoStream = stream; // Store the stream for later use
                    video.srcObject = stream;
                })
                .catch(function(err) {
                    console.error('Error accessing the camera:', err);
                });

            // Capture image
            document.getElementById('capture-btn').addEventListener('click', function() {
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                // Convert captured image to base64 data
                const imageData = canvas.toDataURL('image/png');

                // Stop the video stream
                stopVideoStream();
                
        $.ajax({
            type: 'POST',
            url: '/uploads',
            data: {"image_data":imageData},
            processData: false,
            contentType: false,
            success: function(response) {

                 
                 const mains=response['data']



              
                const formattedArray = response['data'].map(obj => {
                  const key = Object.keys(obj)[0];
                  const value = obj[key];
                  return `${key}: ${value}`;
                }).join('\n');


            var plant= {'Aloevera':'aloe_vera',  'Curry Leaves':'curry_leaves' , 'Mint':'mint', 'Neem':'neem_leaf', 
            'Papaya':'papaya_leaves','Pattharchatta':'patharchatta' , 'Tulsi':'tulsi_leaf'}
// Display the formatted array in an alert

            // const keys = Object.keys(response['data'][0]);
           
          
            const keys = Object.keys(mains[0]);
              const keyName=keys[0];
              var language_id= $('#dropdownMenuButton').text();
              console.log(language_id);
              if(language_id=='\n    ભાષા\n  '){
                  language_id='gujrati'
              }
              if(language_id=='\n    Language\n  '){
                  language_id='english'
              }
              if(language_id=='\n    भाषा\n  '){
                  language_id='hindi'
              }
          
             alert(formattedArray);
            
             window.location.href = "http://127.0.0.1:5000/profile?plant_name="+plant[keyName]+"&language="+language_id;
        },
        error: function(error) {
            console.error(error);
            // Handle any errors here
        }
        });

            });
        }

        function stopVideoStream() {
            if (videoStream) {
                const tracks = videoStream.getTracks();
                tracks.forEach(function(track) {
                    track.stop(); // Stop each track in the video stream
                });
            }
        }