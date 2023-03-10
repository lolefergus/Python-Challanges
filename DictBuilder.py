def top_note(student):
    note = max(student.get("notes"))

    newRecord = {
        "name":student.get("name"),
        "top_note":note
    }
    return newRecord