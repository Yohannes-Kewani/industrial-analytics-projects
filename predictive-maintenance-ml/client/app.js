function get_machine_type_value(){
    var uiMachineType = document.getElementsByName("uiMachineType");
    for (var i in uiMachineType){
        if (uiMachineType[i].checked){
            return uiMachineType[i].value;
        }
    }
    return -1;
}

function onClickPredictFailure() {
    var type = get_machine_type_value();
    var air_T = document.getElementById("uiAir_T");
    var process_T = document.getElementById("uiProcess_T");
    var rpm = document.getElementById("uiRPM");
    var torque = document.getElementById("uiTorque");
    var tool_wear = document.getElementById("uiToolWear");
    var estPrice = document.getElementById("uiEstimateFailure");

    // var url = "http://127.0.0.1:5000/get_failure";
    var url = "/api/get_failure";
    $.post(url, {
        type: type,
        air_T: parseFloat(air_T.value),
        process_T: parseFloat(process_T.value),
        rotational_speed: parseFloat(rpm.value),
        torque: parseFloat(torque.value),
        tool_wear: parseFloat(tool_wear.value)
    },  function(data, status) {
        console.log(data.estimated_failure);
        
        var failureResult = data.estimated_failure;
        var displayMessage = "Unknown";
        var textColor = "black"; // Default color

        if (failureResult === 0) {
            displayMessage = "No Failure";
            textColor = "green"; 
        } else if (failureResult === 1) {
            displayMessage = "Machine Failure";
            textColor = "red"; 
        }

        estPrice.innerHTML = "<h2 style='color: " + textColor + ";'>" + displayMessage + "</h2>";
        console.log(status); });    
}
