const currentYear = new Date().getFullYear


const lastModified = new (Date)
const formattedDate = lastModified.toLocaleDateString('en-US', {
    month: '2-digit',
    day: '2-digit',
    year: 'numeric',
}
);

document.getElementById("lastModified").innerHTML = document.lastModified