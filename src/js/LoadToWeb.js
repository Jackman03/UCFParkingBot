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
        ${garage.GarageAvailibility}<br>
        ${garage.TotalOccupied}<br>
        ${garage.AmountChanged}
        `;

        container.appendChild(garageDiv);
    });
}
/*
function displayGarages(garages) {
    const container = document.getElementById('garages-container');
    garages.forEach(garage => {
        // Create a new div element for each garage with a unique id (based on the garage code)
        const garageDiv = document.createElement('div');
        garageDiv.classList.add('garage');
        garageDiv.id = `garage-${garage.code}`.trip();  // Unique id for each garage

        // Insert garage data into the div
        garageDiv.innerHTML = `
            <h2>${garage.name} (${garage.code})</h2>
            <p><strong>Location:</strong> ${garage.location}</p>
            <p><strong>Capacity:</strong> ${garage.capacity} cars</p>
        `;

        // Append the new div to the container
        container.appendChild(garageDiv);
    });
}
*/

/*
Garage =>
            {
            list.insertAdjacentHTML('beforeend',
            `<dt> Garage Name: ${Garage.GarageName}</dt>
                <dd>Availibility: ${Garage.GarageAvailibility}</dd>
                <dd>Spots Occupied: ${Garage.TotalOccupied}</dd>
                <dd>Amount Changed: ${Garage.AmountChanged} <br><br>`
                );    
        })




`<p> Garage Name: ${garage.GarageName}</p>
                <br><p>Availibility: ${garage.GarageAvailibility}\n</p></br>
                <p>Spots Occupied: ${garage.TotalOccupied}</p>
                <p>Amount Changed: ${garage.AmountChanged} <p>`;



                */