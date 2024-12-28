//load the JSON Garage file


const list = document.querySelector('dl');


fetch("../data/Garages.json")
    .then(res => res.json())
    .then(data =>{
        displayGarages(data)
    })
    .catch(error=> console.error("Error loading JSON",error));


function displayGarages(garages) {
    const container = document.getElementById('garages-container');
    garages.forEach(garage => {
        const garageDiv = document.createElement('div');
        garageDiv.classList.add('garage');
        //garageDiv.class = `${garage.GarageName}`.replace(/\s/g, '');
        garageDiv.classList.add(`${garage.GarageName}`.replace(/\s/g, ''));
        //for debugging
        console.log(garageDiv.class)
        garageDiv.innerHTML = `${garage.GarageName} <br>
        open: ${garage.GarageAvailibility}<br>
        occupied: ${garage.TotalOccupied}<br>
        changed: ${garage.AmountChanged} 
        `;

        container.appendChild(garageDiv);
    });
}