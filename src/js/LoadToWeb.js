//load the JSON Garage file


const list = document.querySelector('dl');
const time = document.querySelector('p');


fetch("../data/Garages.json")
    .then(res => res.json())
    .then(data =>{
        console.log(data)
        data.forEach(Garage =>{
            list.insertAdjacentHTML('beforeend',`<dt> Garage Name: ${Garage.GarageName}</dt>
                <dd>Availibility: ${Garage.GarageAvailibility}</dd>
                <dd>Spots Occupied: ${Garage.TotalOccupied}</dd>
                <dd>Amount Changed: ${Garage.AmountChanged} <br><br>`);
                
        })
    });


