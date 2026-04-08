const displayVisit = document.querySelector(".reviewsN");

let visitsNum = Number(window.localStorage.getItem("reviews-counts")) || 0;

if (visitsNum !== 0) {
    displayVisit.textContent = visitsNum;
} else {
    displayVisit.textContent = `Welcome, this is your first review!!`
}

visitsNum++;

localStorage.setItem("reviews-counts", visitsNum)


