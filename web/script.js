function loadBullionData() {
    fetch("../data/bullion.json")
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#bullionTable tbody");
            tbody.innerHTML = ""; // Clear old rows
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
        .catch(err => console.error("Error loading JSON:", err));

    // Update screenshot link
    fetch("../data/screenshots/") // get folder listing (we’ll handle below)
        .then(() => {
            // For simplicity, always link the latest timestamped screenshot manually
            // Assuming scraper runs every 2 minutes
            const now = new Date();
            const timestamp = now.toISOString().replace(/[-:]/g,"").slice(0,15); // approximate
            const link = document.getElementById("screenshotLink");
            link.href = `../data/screenshots/bullion_${timestamp}.png`;
        });
}

// Load data immediately
loadBullionData();

// Refresh every 2 minutes (120000 ms)
setInterval(loadBullionData, 120000);
