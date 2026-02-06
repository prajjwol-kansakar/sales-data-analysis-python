function runScraperThenLoad() {
    fetch("/run-scraper")
        .then(res => res.json())
        .then(() => loadBullionData())
        .catch(err => console.error(err));
}

function loadBullionData() {
    fetch("/api/bullion")
        .then(res => res.json())
        .then(data => {
            const tbody = document.querySelector("#bullionTable tbody");
            tbody.innerHTML = "";
            data.forEach(item => {
                tbody.innerHTML += `
                  <tr>
                    <td>${item.Name}</td>
                    <td>${item.Price}</td>
                    <td>${item["Daily Change"]}</td>
                  </tr>`;
            });
        });
}

runScraperThenLoad();
