() => {
    const stops = document.querySelector('[href^=\"#RoutesStopOnRidePlace\"]').parentElement.parentElement.parentElement.parentElement.parentElement.childNodes;
    let data = {};

    for (const stop of stops) {
        const stopName = stop.childNodes[0].textContent;
        const times = stop.childNodes[2].childNodes;
        let localData = [];

        for (const time of times) {
            const timeDetails = time.querySelectorAll(".gwt-Label, .gwt-Anchor");
            let localTimes = {};
            let pairedKey = "";

            for (const timeDetail of timeDetails) {
                const isVisible = timeDetail.parentElement.getAttribute("aria-hidden") !== "true";

                if (isVisible) {
                    if (timeDetail.textContent.includes(":") && !timeDetail.textContent.includes("AM") && !timeDetail.textContent.includes("PM")) {
                        pairedKey = timeDetail.textContent.split(":")[0];
                    } else if (timeDetail.textContent === "On Time") {
                        localTimes["ETA"] = "On Time";
                    } else {
                        localTimes[pairedKey] = timeDetail.textContent;
                    }
                }
            }

            localData.push(localTimes);
        }

        data[stopName] = localData;
    }

    return data;
}
