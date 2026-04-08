const hamButton = document.querySelector('#menu');
const navigation = document.querySelector('.navigation');

hamButton.addEventListener('click', () => {
    navigation.classList.toggle('open');
    hamButton.classList.toggle('open');
});


document.getElementById('indipokemon')

// IA was used to help me to find some code issues but the ideas and logical were written and made by me


const kantoPokemons = [
    {
        name: "Charmander",
        hp: 39,
        attack: 52,
        defense: 43,
        speed: 65,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/4.png"
    },
    {
        name: "Bulbasaur",
        hp: 45,
        attack: 49,
        defense: 49,
        speed: 45,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/1.png"
    },
    {
        name: "Squirtle",
        hp: 44,
        attack: 48,
        defense: 65,
        speed: 43,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/7.png"
    },
];



const johtoPokemons = [

    {
        name: "Cyndaquil",
        hp: 39,
        attack: 52,
        defense: 43,
        speed: 65,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/155.png"
    },

    {
        name: "Totodile",
        hp: 50,
        attack: 65,
        defense: 64,
        speed: 43,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/158.png"
    },

    {
        name: "Chikorita",
        hp: 45,
        attack: 49,
        defense: 65,
        speed: 45,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/152.png"
    },]



const hoenPokemons = [

    {
        name: "Torchic",
        hp: 45,
        attack: 60,
        defense: 40,
        speed: 45,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/255.png"
    },

    {
        name: "Mudkip",
        hp: 50,
        attack: 70,
        defense: 50,
        speed: 40,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/258.png"
    },

    {
        name: "Treecko",
        hp: 40,
        attack: 45,
        defense: 35,
        speed: 70,
        imageUrl:
            "https://easycdn.es/1/poke/i/pokedex/ken/252.png"
    },


];


// Pictures taken from https://pokemaster.es/



function showPokemons(pokemons) {
    const div = document.querySelector('#indipokemon');


    if (!div) return;
    let rows = "";

    for (const pokemon of pokemons) {
        rows += `
      <div class = 'indie'>
                    <img loading="lazy" src="${pokemon.imageUrl}" alt="${pokemon.name}">
                <ul class="infop">
                    <li><strong>Name:</strong> ${pokemon.name}</li>
                    <li><strong>HP:</strong> ${pokemon.hp}</li>
                    <li><strong>ATK:</strong> ${pokemon.attack}</li>
                    <li><strong>DEF:</strong> ${pokemon.defense}</li>
                    <li><strong>SPD:</strong> ${pokemon.speed}</li>
                </ul> 
            </div>
`}
    div.innerHTML = rows;
}


///////////////////////////////////////////////////////////////////


function sumPower(pokemon) {

    let power = pokemon.hp + pokemon.attack + pokemon.defense + pokemon.speed;
    return power
}

function computeStronger(pokemons) {
    let stronger = pokemons[0];

    pokemons.forEach(pokemon => {

        if (sumPower(pokemon) > sumPower(stronger)) {
            stronger = pokemon;
        }
    });
    return stronger
}

function recommended(stronger) {
    const div = document.querySelector('#recomendation');

    if (!div) return;
    let rows = "";

    rows += `
      <div>
                    <img loading="lazy" src="${stronger.imageUrl}" alt="${stronger.name}">
                <ul class="infop">
                    <li><em><strong>${stronger.name}</strong></em></li>
                    
`
    div.innerHTML = rows;
}







const savedData = JSON.parse(localStorage.getItem('user_selection'))

if (savedData && savedData.region) {
    const region = savedData.region


    if (region === "kanto") {
        showPokemons(kantoPokemons)
        stronger = computeStronger(kantoPokemons)
        recommended(stronger)
    }


    else if (region === "johto") {
        showPokemons(johtoPokemons)
        stronger = computeStronger(johtoPokemons)
        recommended(stronger)
    }

    else if (region === 'hoen') {
        showPokemons(hoenPokemons)
        stronger = computeStronger(hoenPokemons)
        recommended(stronger)
    }


}




