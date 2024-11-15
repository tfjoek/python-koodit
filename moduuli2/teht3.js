let dogNames = [];
for (let i = 0; i < 6; i++) {
    let dogName = prompt(`Enter dog name ${i + 1}:`);
    dogNames.push(dogName);
}
dogNames.sort().reverse();
let ul = document.createElement('ul');
dogNames.forEach(dog => {
    let li = document.createElement('li');
    li.textContent = dog;
    ul.appendChild(li);
});
document.body.appendChild(ul);
