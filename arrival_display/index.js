const dateElement = document.querySelector("#date");
const timeElement = document.querySelector("#time");
const arrivalsList = document.querySelector(".arrivals-list");
const noService = document.querySelector("#no-arrivals");
const stopTitle = document.querySelector("#stop-name");
const configuredStop = decodeURI(window.location.href.split("?stop=")[1]);
stopTitle.textContent = configuredStop;

const updateDate = () => {
    const date = new Date();
    dateElement.textContent = date.toLocaleDateString();
    timeElement.textContent = date.toLocaleTimeString();
}

const updateArrivals = async () => {
    console.log("Updating arrivals...");

    fetch("http://tripshot.taila93dbf.ts.net:5000/get_all_route_times", {
        method: "GET" //,
        // "headers": {"route": configuredRoute}
    }).then((res) => {
        res.json().then((data) => {
            // Clean elements first
            let didWriteData = false;

            for (const el of document.querySelectorAll(".arrival-item")) {
                el.remove();
            }

            for (const busRoute of Object.keys(data)) {
                if (Object.keys(data[busRoute]).includes(configuredStop)) {
                    for (let i = 0; i <= data[busRoute][configuredStop].length; i++) {
                        const cloneElement = document.querySelector("#dummy");
                        const el = cloneElement.cloneNode(true);
                        const currentData = data[busRoute][configuredStop][i];

                        if (currentData && Object.keys(currentData).includes("Scheduled")) {
                            const baseData = data[busRoute][configuredStop][i];
                            let arrivalTime = Object.keys(baseData).includes("ETA") ? baseData["ETA"] : baseData["Scheduled"];
                            
                            if (arrivalTime == "On Time") {
                                arrivalTime = baseData["Scheduled"];
                                el.classList.add("bus-on-time");
                            } else if (arrivalTime == "At Stop") {
                                arrivalTime = "Boarding";
                                el.classList.add("bus-boarding");
                            } else if (arrivalTime != baseData["Scheduled"]) {
                                el.classList.add("bus-late");
                            }

                            if (arrivalTime.includes(":")) {
                                const match = arrivalTime.trim().match(/^(\d{1,2}):(\d{2})\s*(AM|PM)$/i);

                                let hours = parseInt(match[1], 10);
                                const minutes = parseInt(match[2], 10);
                                const period = match[3].toUpperCase();

                                if (period === 'PM' && hours !== 12) {
                                    hours += 12;
                                } else if (period === 'AM' && hours === 12) {
                                    hours = 0;
                                }

                                const targetMinutes = hours * 60 + minutes;

                                const now = new Date();
                                const currentMinutes = now.getHours() * 60 + now.getMinutes();

                                const diffMinutes = Math.abs(currentMinutes - targetMinutes);
                                arrivalTime = diffMinutes + " min" + (diffMinutes != 1 ? "s" : "");
                            }

                            el.removeAttribute("id");
                            el.querySelector(".arrival-route").textContent = busRoute;
                            el.querySelector(".arrival-time").textContent = arrivalTime;
                            el.classList.add("arrival-item");

                            arrivalsList.appendChild(el);

                            didWriteData = true;
                        }
                    }
                }

                noService.style.display = (didWriteData ? "none" : "block");
            }
        });
    });
}

// Update on page startup
updateDate();
updateArrivals();

// Schedule updates for these intervals
setInterval(updateDate, 500);
setInterval(updateArrivals, 10000);
