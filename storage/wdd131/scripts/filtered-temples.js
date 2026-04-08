const hamButton = document.querySelector('#menu');
const navigation = document.querySelector('.navigation');

hamButton.addEventListener('click', () => {
    navigation.classList.toggle('open');
    hamButton.classList.toggle('open');
});



// ///////////////////////////////////////////////////////////////////////////////////////////////////

const temples = [
    {
        templeName: "Aba Nigeria",
        location: "Aba, Nigeria",
        dedicated: "2005, August, 7",
        area: 11500,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/aba-nigeria/400x250/aba-nigeria-temple-lds-273999-wallpaper.jpg"
    },
    {
        templeName: "Manti Utah",
        location: "Manti, Utah, United States",
        dedicated: "1888, May, 21",
        area: 74792,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/manti-utah/400x250/manti-temple-768192-wallpaper.jpg"
    },
    {
        templeName: "Payson Utah",
        location: "Payson, Utah, United States",
        dedicated: "2015, June, 7",
        area: 96630,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/payson-utah/400x225/payson-utah-temple-exterior-1416671-wallpaper.jpg"
    },
    {
        templeName: "Yigo Guam",
        location: "Yigo, Guam",
        dedicated: "2020, May, 2",
        area: 6861,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/yigo-guam/400x250/yigo_guam_temple_2.jpg"
    },
    {
        templeName: "Washington D.C.",
        location: "Kensington, Maryland, United States",
        dedicated: "1974, November, 19",
        area: 156558,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/washington-dc/400x250/washington_dc_temple-exterior-2.jpeg"
    },
    {
        templeName: "Lima Perú",
        location: "Lima, Perú",
        dedicated: "1986, January, 10",
        area: 9600,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/lima-peru/400x250/lima-peru-temple-evening-1075606-wallpaper.jpg"
    },
    {
        templeName: "Mexico City Mexico",
        location: "Mexico City, Mexico",
        dedicated: "1983, December, 2",
        area: 116642,
        imageUrl:
            "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/mexico-city-mexico/400x250/mexico-city-temple-exterior-1518361-wallpaper.jpg"
    },

    {
        templeName: "Kirtland US",
        location: "Kirtland, US",
        dedicated: "1836, March, 27",
        area: 11610,
        imageUrl:
            "https://churchofjesuschristtemples.org/assets/img/temples/kirtland-temple/kirtland-temple-1275-main.jpg"
    },

    {
        templeName: "Guatemala City Guatemala",
        location: "Guatemala, City Guatemala",
        dedicated: "1984, December, 14",
        area: 116642,
        imageUrl:
            "https://churchofjesuschristtemples.org/assets/img/temples/guatemala-city-guatemala-temple/guatemala-city-guatemala-temple-6415-main.jpg"
    },

    {
        templeName: "Tokyo Japan",
        location: "Tokyo, Japan",
        dedicated: "1980, October, 27",
        area: 5016,
        imageUrl:
            "https://churchofjesuschristtemples.org/assets/img/temples/tokyo-japan-temple/tokyo-japan-temple-26340-main.jpg"
    },
    // Add more temple objects here...
];




function showTemples(theTemple) {

    const div =
        document.querySelector("#temple-java");
    let rows = "";
    for (const aTemple of theTemple) {
        rows += `
<figure>
    
        <figcaption>${aTemple.templeName}</figcaption>
        <p><span>Location: </span>${aTemple.location}</p>
        <p><span>Dedicated: </span>${aTemple.dedicated}</p>
        <p><span>Size: </span>${aTemple.area} sq ft</p>
    
        <img loading="lazy" src="${aTemple.imageUrl}" alt="${aTemple.templeName}">
</figure>
`
    }
    div.innerHTML = rows;

}



showTemples(temples);


// /////////////////////////////////////////////////////////////////////////////////////////////

const filtered = (number) => {

}

const oldTemplesLink = document.querySelector("#oldTemples")

oldTemplesLink.addEventListener("click", () => {
    const oldTemples = temples.filter(temple => {
        let dedicatedNumber = parseInt(temple.dedicated.split(',')[0]);
        return dedicatedNumber < 1900
    })
    showTemples(oldTemples);
});


const homeLink = document.querySelector("#home")

homeLink.addEventListener("click", () => {
    showTemples(temples);;
});


const newLink = document.querySelector("#new")

newLink.addEventListener("click", () => {
    const newTemplates = temples.filter(temple => {
        let dedicatedNumber = parseInt(temple.dedicated.split(',')[0]);
        return dedicatedNumber > 2000
    })
    showTemples(newTemplates);
});

const largeLink = document.querySelector("#large")

largeLink.addEventListener("click", () => {
    const largeTemplates = temples.filter(temple => {
        let dedicatedNumber = temple.area;
        return dedicatedNumber > 10000
    })
    showTemples(largeTemplates);
});


const smallLink = document.querySelector("#small")

smallLink.addEventListener("click", () => {
    const smallTemplates = temples.filter(temple => {
        let dedicatedNumber = temple.area;
        return dedicatedNumber <= 10000
    })
    showTemples(smallTemplates);
});


//document.querySelector(".res-grid").innerHTML = "";  PARA LIMPIAR