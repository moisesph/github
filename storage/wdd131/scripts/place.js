//Calculate the WindChill


let temperature = -21;
let wind = 4.83;


function calculateWindChill(temperature, wind) {

    return windChill = temperature - wind;
};


let windChillShow = calculateWindChill(temperature, wind)

document.getElementById("words").innerHTML = `Wind Chill:`;
if (temperature <= 10 && wind > 4.8) {
    document.getElementById("windChill").innerHTML = `${windChillShow} °C`;
}
else { document.getElementById("windChill").innerHTML = `N/A` }



document.getElementById("temperatureVariable").innerHTML = `${temperature} °C`;

let windRounded = wind.toFixed(2)
document.getElementById("windVariable").innerHTML = `${windRounded}`;
