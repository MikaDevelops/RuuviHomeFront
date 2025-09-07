async function getData(startTime, endTime, loginToken=0){
    let fetchUrl = `data?from=${startTime}&to=${endTime}&token=${loginToken}`;
    let response = await fetch(fetchUrl);
    if (!response.ok) throw new Error (`response status: ${response.status}`);
    return await response.text();
}