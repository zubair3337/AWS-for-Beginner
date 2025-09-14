function printMonthCalendar(month, year) {
    // Get the first day and the total days of the given month
    const firstDay = new Date(year, month, 1).getDay(); // Day of the week (0 = Sunday, 1 = Monday, etc.)
    const daysInMonth = new Date(year, month + 1, 0).getDate(); // Total days in the month

    // Weekday names
    const weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

    // Print weekday headers
    console.log(weekdays.join(" "));

    // Start printing the calendar
    let calendar = "";
    let currentDay = 1;

    // Add leading spaces for days before the 1st of the month
    for (let i = 0; i < firstDay; i++) {
        calendar += "    "; // Add spacing for empty days
    }

    // Add days of the month
    for (let i = firstDay; currentDay <= daysInMonth; i++) {
        calendar += currentDay.toString().padStart(2, " ") + "  "; // Add the day number with padding
        currentDay++;

        // Break the line after Saturday (6)
        if (i % 7 === 6) {
            calendar += "\n";
        }
    }

    console.log(calendar);
}

// Usage example: Print the calendar for December 2024
printMonthCalendar(11, 2024); // Month is zero-based, so 11 = December
