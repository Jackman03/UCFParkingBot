//Program to get thr last time the garages were updates

function GetLastTime(){

    let PrevTime = new Date(new Date().getTime() - 0.25*60*60*1000).toLocaleTimeString();

    console.log(PrevTime)
    document.write(PrevTime)

}

GetLastTime()