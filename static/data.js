async function getData(startTime, endTime, loginToken=0){
    let fetchUrl = `data?from=${startTime}&to=${endTime}&token=${loginToken}`;
    let response = await fetch(fetchUrl);
    if (!response.ok) throw new Error (`response status: ${response.status}`);
    let responseObj = await response.json();
    return responseObj;
}

function makeHeaderRow(columns){
    let headerRow = document.createElement('tr');
    for (column of columns){
        let cell = document.createElement('th');
        cell.innerText = column;
        headerRow.appendChild(cell);
    }
    return headerRow;
}

function renderTableToPage(areaId, dataToRender){
    if (dataToRender.length = 0) return;
    //mock
    dataToRender = [
        {
            epochTime: 1757874070,
            humidity: 57.42,
            temperature:20.26,
            pressure:1005.86,
            acceleration:1020.5723884174,
            acceleration_x:12,
            acceleration_y:-32,
            acceleration_z:-1020,
            tx_power:4,
            battery:2886,
            movement_counter:86,
            measurement_sequence_number:5682,
            mac:'acb595fb4f72',
            rssi:-83
        },
        {
            epochTime: 1757878070,
            humidity: 56.32,
            temperature:23.26,
            pressure:1002.78,
            acceleration:1020.5723884174,
            acceleration_x:12,
            acceleration_y:-32,
            acceleration_z:-1020,
            tx_power:4,
            battery:2886,
            movement_counter:86,
            measurement_sequence_number:562,
            mac:'d72deadfd23b',
            rssi:-83
        }
    ];
    let table = document.createElement('table');
    let columnNames = Object.keys(dataToRender[0]);
    let headerRow = makeHeaderRow(columnNames);
    table.appendChild(headerRow);
    let area = document.getElementById(areaId);
    area.appendChild(table);
    //area.replaceChildren([table]);
}