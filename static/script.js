function loadBullionData() {
    fetch("/api/bullion")
        .then(res => res.json())
        .then(data => {
            const tbody = document.querySelector("#bullionTable tbody");
            tbody.innerHTML = "";
            data.forEach(item => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${item.Name}</td>
                    <td>${item.Price}</td>
                    <td>${item["Daily Change"]}</td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(err => console.error(err));

    fetch("/api/latest-screenshot")
        .then(res => res.json())
        .then(data => {
            if (data.url) {
                document.getElementById("screenshotLink").href = data.url;
            }
        });
}

loadBullionData();
setInterval(loadBullionData, 120000);
