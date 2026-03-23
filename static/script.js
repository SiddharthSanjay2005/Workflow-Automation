function addLead() {
    fetch("/add-lead", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: document.getElementById("name").value,
            phone: document.getElementById("phone").value,
            status: document.getElementById("status").value,
            interest_level: parseInt(document.getElementById("interest").value)
        })
    })
    .then(res => res.json())
    .then(() => loadLeads());
}

function loadLeads() {
    fetch("/leads")
    .then(res => res.json())
    .then(data => {
        const table = document.getElementById("leadTable");
        table.innerHTML = "";

        data.leads.forEach(l => {
            table.innerHTML += `
                <tr>
                    <td>${l.name}</td>
                    <td>${l.status}</td>
                    <td>${l.interest_level}</td>
                </tr>
            `;
        });
    });
}

function loadLogs() {
    fetch("/logs")
    .then(res => res.json())
    .then(data => {
        document.getElementById("logs").innerText =
            JSON.stringify(data.logs, null, 2);
    });
}

window.onload = loadLeads;