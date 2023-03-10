let theWheel = new Winwheel({
    'canvasId'    : 'canvas',
    'numSegments' : 8,
    'innerRadius' : 10,// Set inner radius as number.
    'responsive'   : true,  // This wheel is responsive!
    'segments'    :
    [
        {'fillStyle' : '#eae56f', 'text' : 'yvan'},
        {'fillStyle' : '#89f26e', 'text' : 'derick'},
        {'fillStyle' : '#7de6ef', 'text' : 'laugan'},
        {'fillStyle' : '#e7706f', 'text' : 'kyd'},
        {'fillStyle' : '#eae56f', 'text' : 'pacha'},
        {'fillStyle' : '#89f26e', 'text' : 'deku'},
        {'fillStyle' : '#7de6ef', 'text' : 'allmight'},
        {'fillStyle' : '#e7706f', 'text' : 'oneforall'}
    ],
    'lineWidth'   : 2 ,
    'animation' :                   // Note animation properties passed in constructor parameters.
    {
        'type'     : 'spinToStop',  // Type of animation.
        'duration' : 5,             // How long the animation is to take in seconds.
        'spins'    : 20,           // The number of complete 360 degree rotations the wheel is to do.   
        'callbackSound' : playSound,    // Specify function to call when sound is to be triggered.
        'callbackFinished' : 'alertPrize()', // Remember to do something after the animation has finished specify callback function.
    },
    'pins' :    // Specify pin parameters.
    {
        'number'      : 18,
        'outerRadius' : 5,
        'margin'      : 8,
        'fillStyle'   : '#ffffff',
        'strokeStyle' : '#008080',
        'responsive'   : true,  // This wheel is responsive!
    }
});
function alertPrize()
{
    // Call getIndicatedSegment() function to return pointer to the segment pointed to on wheel.
    let winningSegment = theWheel.getIndicatedSegment();

    // Basic alert of the segment text which is the prize name.
    alert("Vous offrirez un cadeau à  " + winningSegment.text + "!");
    //console.log(winningSegment.text);
}

let audio = new Audio('static/audio/Amir.mp3');  // Create audio object and load desired file.
    
 
    function playSound()
    {
        // Stop and rewind the sound (stops it if already playing).
        audio.pause();
        audio.currentTime = 0;
 
        // Play the sound.
        audio.play();
    }
