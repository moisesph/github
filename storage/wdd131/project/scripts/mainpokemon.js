// IA was used to help me to remember how to use JSON and the construction of the code but the logic was made for me


const regionUsed = document.getElementById('sub-region');



regionUsed.addEventListener('submit', function (event) {

    const actualRegion = new FormData(regionUsed);
    const selectedRegion = actualRegion.get('regionSelected')

    const infoData = {
        region: selectedRegion
    }

    const jsonString = JSON.stringify(infoData)

    localStorage.setItem('user_selection', jsonString);


})

