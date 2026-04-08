const input = document.querySelector('#favchap');
const button = document.querySelector('button');
const list = document.querySelector('#list');

let chaptersArray = getChapterList() || [];

chaptersArray.forEach(chapter => {
    displayList(chapter);
});



function displayList(item) {
    let li = document.createElement('li');
    let deleteButton = document.createElement('button');
    li.textContent = item;
    deleteButton.textContent = '❌'
    deleteButton.classList.add('delete');
    li.append(deleteButton);
    list.append(li)

    deleteButton.addEventListener('click', function () {
        list.removeChild(li);
        deleteChapter(li.textContent);
        input.focus();
    })
}

setChapterList = () => localStorage.setItem('favBook', JSON.stringify(chaptersArray));




function deleteChapter(chapter) {
    chapter = chapter.slice(0, chapter.length – 1);
    chaptersArray = chaptersArray.filter(item => item !== chapter);
    setChapterList();
}


button.addEventListener('click', function () {
    if (input.value.trim() !== '') {
        const li = document.createElement('li');
        li.textContent = input.value;
        const deleteButton = document.createElement('button');
        deleteButton.textContent = '❌';
        li.append(deleteButton);
        list.append(li);
        input.value = ''
        input.focus();
    };
});


list.addEventListener('click', function (e) {
    if (chaptersArray.length === 0) {
        displayList(input.value);
        chaptersArray(input.value);
        setChapterList();
        input.value = '';
        input.focus();
    }
})