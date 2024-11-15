let numParticipants = prompt("How many participants?");
let participants = [];

for (let i = 0; i < numParticipants; i++) {
    let name = prompt(`Enter name of the participant ${i + 1}:`);
    participants.push(name);
}
participants.sort();
let ol = document.createElement('ol');
participants.forEach(name => {
    let li = document.createElement('li');
    li.textContent = name;
    ol.appendChild(li);
});

document.body.appendChild(ol);
