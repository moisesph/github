let names = ['Nancy', 'Blessing', 'Jorge', 'Svetlana', 'Bob'];
const initialValue = 0;



let namesB = names.filter(name => name.charAt(0) == 'B');
//console.log(namesB);


let namesLength = names.map(name => name.length);




let averageLength = names.reduce(
    (average, name) => average + name.length,
    initialValue,
) / names.length;



console.log(averageLength);
