def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error : template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error : attendees must be a list")
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error : attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty no output files generated")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated")
        return
    for i, attendee in enumerate(attendees, start=1):
        content = template

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_location = attendee.get("event_location") or "N/A"
        event_date = attendee.get("event_date") or "N/A"

        content = content.replace("{name}", name)
        content = content.replace("{event_date}", event_date)
        content = content.replace("{event_title}", event_title)
        content = content.replace("{event_location}", event_location)

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w") as file :  
                file.write(content)
        except Exception as e:
            print(f"Error writing file : {filename}: {e}")