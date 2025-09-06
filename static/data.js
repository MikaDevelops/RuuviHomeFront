async function getData(startTime, endTime, loginToken){
    let fetchUrl = `127.0.0.1:5000/getdata?from=${startTime}&to=${endTime}$token=${loginToken}`;
    fetch()
}